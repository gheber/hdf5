#!/usr/bin/env python3
"""
CMake SBOM Generator
Generates SBOM from CMake build information
"""
import json
import re
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
class CMakeSBOMGenerator:
    def __init__(self, build_dir, target_name):
        self.build_dir = Path(build_dir)
        self.target_name = target_name
        self.compile_commands = self._load_compile_commands()
    def generate_sbom(self, output_file):
        """Generate SBOM from CMake build information"""
        # Load base metadata
        metadata_file = self.build_dir / "sbom_metadata.json"
        with open(metadata_file) as f:
            metadata = json.load(f)
        # Create SPDX document
        sbom = {
            "SPDXID": "SPDXRef-DOCUMENT",
            "spdxVersion": "SPDX-2.3",
            "creationInfo": {
                "creators": [
                    "Tool: cmake-sbom-generator",
                    f"Tool: CMake-{metadata['build_info']['cmake_version']}"
                ],
                "created": datetime.utcnow().isoformat() + "Z"
            },
            "name": metadata["project"]["name"],
            "documentNamespace": f"https://cmake.org/{metadata['project']['name']}-{self._generate_uuid()}",
            "packages": [],
            "relationships": []
        }
        # Add root package
        root_package = self._create_root_package(metadata)
        sbom["packages"].append(root_package)
        # Extract dependencies from compile commands
        dependencies = self._extract_dependencies()
        for dep in dependencies:
            spdx_package = self._create_dependency_package(dep)
            sbom["packages"].append(spdx_package)
            # Add relationship
            sbom["relationships"].append({
                "spdxElementId": "SPDXRef-RootPackage",
                "relatedSpdxElement": spdx_package["SPDXID"],
                "relationshipType": "DEPENDS_ON"
            })
        # Write SBOM
        with open(output_file, 'w') as f:
            json.dump(sbom, f, indent=2)
        print(f"Generated CMake SBOM: {output_file}")
    def _load_compile_commands(self):
        """Load compile_commands.json if available"""
        compile_commands_file = self.build_dir / "compile_commands.json"
        if compile_commands_file.exists():
            with open(compile_commands_file) as f:
                return json.load(f)
        return []
    def _extract_dependencies(self):
        """Extract dependencies from CMake targets and compile commands"""
        dependencies = set()
        # Parse compile commands for include paths and libraries
        for command in self.compile_commands:
            cmd_line = command.get("command", "")
            # Extract include directories
            include_paths = re.findall(r'-I([^\s]+)', cmd_line)
            for include_path in include_paths:
                dep_name = self._guess_library_name(include_path)
                if dep_name:
                    dependencies.add(dep_name)
            # Extract linked libraries
            libraries = re.findall(r'-l([^\s]+)', cmd_line)
            dependencies.update(libraries)
        # Try to get more info from CMake cache
        cmake_cache = self._parse_cmake_cache()
        dependencies.update(self._extract_from_cache(cmake_cache))
        return [{"name": dep, "type": "library"} for dep in dependencies]
    def _guess_library_name(self, include_path):
        """Guess library name from include path"""
        path = Path(include_path)
        # Common patterns
        if "boost" in path.name.lower():
            return "boost"
        elif "openssl" in path.name.lower():
            return "openssl"
        elif "curl" in path.name.lower():
            return "libcurl"
        elif "protobuf" in path.name.lower():
            return "protobuf"
        return None
    def _parse_cmake_cache(self):
        """Parse CMakeCache.txt for dependency information"""
        cache_file = self.build_dir / "CMakeCache.txt"
        cache_data = {}
        if cache_file.exists():
            with open(cache_file) as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        cache_data[key] = value
        return cache_data
    def _extract_from_cache(self, cache_data):
        """Extract dependency information from CMake cache"""
        dependencies = set()
        for key, value in cache_data.items():
            # Look for package-related cache entries
            if "_DIR" in key and "FOUND" not in key:
                package_name = key.replace("_DIR", "").lower()
                if package_name not in ["cmake", "cpack", "ctest"]:
                    dependencies.add(package_name)
            elif "_FOUND" in key and value == "TRUE":
                package_name = key.replace("_FOUND", "").lower()
                dependencies.add(package_name)
        return dependencies
    def _create_root_package(self, metadata):
        """Create root package from metadata"""
        return {
            "SPDXID": "SPDXRef-RootPackage",
            "name": metadata["project"]["name"],
            "versionInfo": metadata["project"]["version"],
            "downloadLocation": "NOASSERTION",
            "filesAnalyzed": True,
            "copyrightText": "NOASSERTION"
        }
    def _create_dependency_package(self, dep):
        """Create SPDX package for dependency"""
        return {
            "SPDXID": f"SPDXRef-{dep['name']}",
            "name": dep["name"],
            "versionInfo": "NOASSERTION",
            "downloadLocation": "NOASSERTION", 
            "filesAnalyzed": False,
            "copyrightText": "NOASSERTION",
            "externalRefs": [
                {
                    "referenceCategory": "PACKAGE-MANAGER",
                    "referenceType": "cmake",
                    "referenceLocator": f"cmake:{dep['name']}"
                }
            ]
        }
    def _generate_uuid(self):
        """Generate UUID for document namespace"""
        import uuid
        return str(uuid.uuid4())
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate SBOM from CMake build")
    parser.add_argument("--build-dir", required=True, help="CMake build directory")
    parser.add_argument("--target", required=True, help="CMake target name")
    parser.add_argument("--output", required=True, help="Output SBOM file")
    args = parser.parse_args()
    generator = CMakeSBOMGenerator(args.build_dir, args.target)
    generator.generate_sbom(args.output)
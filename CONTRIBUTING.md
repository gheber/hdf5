# How to Contribute to HDF5

We welcome contributions to the HDF5 project and appreciate efforts ranging from minor typo corrections to new features. This guide outlines the process and principles for contributing to HDF5. If you have questions or need guidance, feel free to reach out.

## Contribution Requirements

Before contributing, you must agree to the HDF Group software license terms found in the LICENSE file in each branch's top-level directory.

> **Prerequisite**: Familiarity with `git` and `GitHub`. If you are new, review the [GitHub tutorial](https://guides.github.com/activities/hello-world/), which takes about 10 minutes.

## Table of Contents

1. [Workflow](#workflow)
2. [Acceptance Criteria](#acceptance-criteria)
3. [Release Notes](#release-notes)
4. [Checklist](#checklist)

## Workflow

Follow these steps to contribute:

1. **Open an Issue**:
   - Create an issue on [HDF5 GitHub](https://github.com/HDFGroup/hdf5/issues) unless the change is minor (e.g., typo fixes).

2. **Fork and Modify**:
   - Fork the [HDF5 repository](https://github.com/HDFGroup/hdf5).
   - Make changes:
     - New features should go to the `develop` branch first, then merge into maintenance branches as needed.
     - Bug fixes should target all relevant branches (`develop` and maintenance).

3. **Build and Test**:
   - Follow instructions in the `INSTALL*` files in the `release_docs` directory to build and test changes.

4. **Push Changes**:
   - Push your changes to GitHub and open a pull request.

5. **Address Feedback**:
   - Ensure your pull request passes CI tests and meets the acceptance criteria outlined below.

## Acceptance Criteria

Contributions are evaluated based on the following:

- **Clear Purpose**: Each pull request must address a specific problem or improvement with clear benefits to the community.
- **Documentation**: Code changes must be documented to explain both the "what" and "how" for future maintenance.
- **Testing**: Contributions must include relevant tests and pass regression testing. Comprehensive multi-platform testing is not expected before submission.
- **Backward Compatibility**: Changes must maintain compatibility with existing HDF5 files and APIs:
  - All files created with HDF5 must remain readable by future versions.
  - No changes to public APIs or data structures are allowed in maintenance releases.
  - Data must remain machine-independent.
- **New Feature Documentation**: Provide adequate documentation for new features.
- **Reasonable Effort**: The effort required to review a PR should be reasonable relative to The HDF Group's and other contributors's resources, capabilities, and the importance of the obligation.
- **Conflict Resolution**: Parties to a conflict should act honestly and sincerely, obeying the [Contributor Covenant Code of Conduct](https://github.com/HDFGroup/hdf5/blob/develop/CODE_OF_CONDUCT.md), and following the process described in the [HDF Enhancement Proposal (HEP)](https://github.com/HDFGroup/heps) process.

For changes to the data model or file format, consult us beforehand as these are only permitted in new major releases.

## Release Notes

Write a release note for any change visible to users, such as new features, bug fixes, or known issues. Use the following format:

```
- Title/Problem

  Problem/Solution
```

### Elements of a Release Note

- **Title**: Identify the issue category (e.g., bug, enhancement).
- **Problem**: Clearly describe the issue and its impact.
- **Solution**: Explain what was done, its impact, and any workarounds.

Release notes are not required for changes that do not affect functionality, such as comment updates or code refactoring.

## Checklist

### General

- [ ] Does the pull request have a clear purpose and a corresponding GitHub issue?
- [ ] Are all applicable branches targeted (e.g., `develop` and maintenance branches)?
- [ ] Does the pull request adhere to HDF5 best practices (e.g., naming conventions, portability)?

### Code Quality

- [ ] Is the new code sufficiently documented for future maintenance?
- [ ] Does the code comply with API compatibility guidelines ([API Compatibility Macros](https://hdfgroup.github.io/hdf5/develop/api-compat-macros.html))?
- [ ] Are changes mirrored in both Autotools and CMake if applicable?

### Documentation

- [ ] Are changes described in the `release_docs/RELEASE.txt` file?
- [ ] Is the new functionality documented using [Doxygen](https://hdfgroup.github.io/hdf5/develop/_r_m_t.html) in the public header files?
- [ ] Is appropriate community-level documentation provided?

### Testing

- [ ] Are relevant tests included?
- [ ] Has the pull request been checked for potential performance impacts?
- [ ] Does the code pass regression testing?

We are here to help ensure your contributions succeed. Reach out with any questions or concerns.

Thank you for contributing to HDF5!


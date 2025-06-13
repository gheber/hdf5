# Guidelines for Noteworthy Documentation Changes

## Purpose
This guideline helps documentation authors determine which changes should be recorded in the documentation changelog. Noteworthy changes are those that significantly impact how users find, understand, or use HDF5 documentation.

## What Constitutes a Noteworthy Change

### Always Document These Changes

**New Content Additions**
- New tutorial pages or guides
- New code examples demonstrating previously undocumented features
- New sections explaining complex concepts or workflows
- New troubleshooting guides or FAQ entries
- Documentation for newly added HDF5 features or APIs

**Significant Corrections**
- Corrections to incorrect function signatures or parameters
- Fixes to code examples that previously didn't compile or work
- Corrections to performance claims or technical specifications
- Updates to deprecated/removed functionality notices
- Corrections to data type sizes, limits, or constraints

**Structural Improvements**
- Major reorganization of documentation sections
- Creation of new documentation categories or modules
- Changes to navigation structure that affect how users find information
- Addition of new index pages or cross-reference systems

**Breaking Changes**
- Removal of previously documented features
- Changes to documented behavior that might break existing code
- Updates reflecting incompatible API changes
- Modified build or installation instructions

### Consider Documenting These Changes

**Clarifications and Enhancements**
- Significant expansions of existing explanations (>50% new content)
- Addition of diagrams or flowcharts
- New warnings about common pitfalls or gotchas
- Performance tips or best practices sections
- Platform-specific notes that affect a significant user base

**Cross-Reference Improvements**
- Addition of "See Also" sections linking related functionality
- New comparison tables between similar functions/features
- Links to external resources that provide essential context

### Do Not Document These Changes

**Minor Corrections**
- Typo fixes or grammar corrections
- Minor formatting adjustments
- Small clarifications that don't change meaning
- Internal link fixes that don't change user navigation
- Whitespace or indentation changes

**Routine Maintenance**
- Updates to copyright years
- Regeneration with newer Doxygen versions (unless output significantly changes)
- HTML/CSS tweaks that don't affect content
- Fixing broken external links with equivalent replacements

## How to Document Changes

When recording a noteworthy change, include:

1. **Date** - When the change was published: use Doxygen `\date` command
2. **Category** - Type of change (New, Corrected, Improved, Removed)
3. **Component** - Which part of HDF5 is affected (`H5D`, `H5F`, Tools, etc.)
4. **Summary** - Brief description of what changed
5. **Impact** - Why users should care
6. **Version** - HDF5 version(s) affected, if applicable

## Example Entry Format

```
2024-03-15 [New] `H5D` - Added comprehensive tutorial on parallel I/O with datasets
   Impact: Users can now find step-by-step guidance for implementing parallel I/O,
   including example code and performance considerations.
   Affects: HDF5 1.14.x and later

2024-03-10 [Corrected] `H5T` - Fixed incorrect byte order in compound type examples
   Impact: Previous examples would create incorrectly formatted data on big-endian
   systems. Users should review their compound type creation code.
   Affects: All versions
```

## Decision Flowchart

Ask yourself:
1. Will users need to change how they use HDF5 based on this documentation change?
2. Does this help users solve a problem they couldn't solve before?
3. Does this correct information that could have led to errors in user code?
4. Will users save significant time finding information due to this change?
5. Does this document previously undocumented behavior?

If you answer "yes" to any of these questions, the change is likely noteworthy.

## Review Process

Before marking a change as noteworthy:
- Consider the audience: Would typical HDF5 users benefit from knowing about this change?
- Assess the scope: Does it affect a commonly used feature or edge case?
- Evaluate persistence: Is this a temporary note or permanent documentation improvement?

When in doubt, err on the side of inclusion—users can skip irrelevant entries more easily than they can discover undocumented changes.

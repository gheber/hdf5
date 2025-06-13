# Pre-Publication Documentation Checklist

The purpose of this checklist is to maintain the quality of the HDF5 library documentation and prevent the inadvertent introduction of defects.
Every author of documentation changes MUST review the relevant sections of this checklist before creating a pull request.

## Build and Rendering Verification
- [ ] Run Doxygen locally to generate documentation without errors or warnings
- [ ] Verify all pages render correctly in multiple browsers (Chrome, Firefox, Safari, Edge)
- [ ] Check that all images, diagrams, and figures display properly
- [ ] Confirm code examples are syntax-highlighted correctly
- [ ] Test all internal navigation links work as expected
- [ ] Verify external links are valid and use HTTPS where possible

## Content Accuracy
- [ ] Cross-reference all function signatures against current source code
- [ ] Verify parameter names and types match implementation
- [ ] Confirm return values and error codes are accurate
- [ ] Check that version information is correct (added/deprecated/removed tags)
- [ ] Validate all code examples compile and run successfully
- [ ] Ensure mathematical formulas render correctly (if using LaTeX)

## Formatting and Style
- [ ] Follow established documentation style guide consistently
- [ ] Use proper Doxygen commands ( `\param`, `\return`, `\see`, etc.)
- [ ] Maintain consistent capitalization and punctuation
- [ ] Check for proper indentation in code blocks
- [ ] Verify lists and tables format correctly
- [ ] Ensure proper escaping of special characters

## Cross-References and Linking
- [ ] Test all `\ref` and `\see` links point to valid targets
- [ ] Verify group memberships (`\ingroup`) are correct
- [ ] Check that related pages link bidirectionally where appropriate
- [ ] Confirm all cited examples exist and are accessible
- [ ] Validate links to external standards or specifications

## Search and Navigation
- [ ] Test search functionality finds new/modified content
- [ ] Verify new pages appear in appropriate navigation sections
- [ ] Check that deprecated items are properly marked but still findable
- [ ] Ensure module/group hierarchy makes logical sense

## Technical Review
- [ ] Have changes reviewed by subject matter expert (as needed)
- [ ] Verify technical accuracy with engineering team if needed
- [ ] Check for consistency with HDF5 specification documents
- [ ] Ensure thread-safety and parallel I/O notes are accurate where relevant

## Accessibility and Usability
- [ ] Include meaningful alt text for all images
- [ ] Ensure sufficient contrast in any custom styling
- [ ] Check that content is readable without horizontal scrolling
- [ ] Verify code examples use appropriate font size and spacing

## Version Control and Metadata
- [ ] Update `\date` tags where appropriate
- [ ] Include meaningful commit message describing changes
- [ ] Tag documentation for specific HDF5 version if applicable
- [ ] Update `CHANGELOG` or release notes if significant changes

## Final Checks
- [ ] Run spell checker on modified content
- [ ] Search for any `TODO` or `FIXME` comments that shouldn't be published
- [ ] Verify no sensitive information or internal comments remain
- [ ] Test documentation on target hosting platform (not just locally)
- [ ] Clear browser cache and verify everything loads correctly

# Seeburger Map Files

This directory contains Seeburger mapping files used by the Mapping Analyzer.

## Files

- `purchase_order.map` - 850 Purchase Order mapping
- `invoice.map` - 810 Invoice mapping
- `eligibility_request.map` - 270 Healthcare Eligibility Request mapping
- `benefit_enrollment.map` - 834 Benefit Enrollment and Maintenance mapping

## Map File Formats

### Binary Map Files (.map)
- Compiled Seeburger map files
- Used for production mapping
- Version-specific to Seeburger

### XML Map Export (.xml)
- Human-readable format
- Useful for analysis and code generation
- Can be edited with text editor

## Usage in Mapping Analyzer

These maps are analyzed for:
- Segment and field mappings
- Data transformation rules
- Compliance with X12 standards
- Performance optimization opportunities

## Map Structure

A typical map contains:
- **Source Schema** - Input data structure
- **Target Schema** - X12 EDI structure
- **Mapping Rules** - Field transformations and routing
- **Validation Rules** - Data validation logic
- **Error Handling** - Exception handling

## Adding New Maps

When adding a new map file:
1. Export from Seeburger in both .map and .xml formats
2. Include documentation of mapping rules
3. Create corresponding input and output schemas
4. Add tests to validate the mapping
5. Update this README

## Best Practices

- Keep maps organized by transaction type
- Document custom mapping rules
- Version control map changes
- Test maps thoroughly before production
- Maintain schema alignment with maps

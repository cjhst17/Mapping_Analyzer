# JSON Schemas for X12 EDI Validation

This directory contains JSON schemas for validating X12 EDI input and output data.

## Directory Structure

```
schemas/
├── input/       # Input data schemas (source system format)
└── output/      # Output data schemas (X12 EDI format)
```

## Schema Files

### Input Schemas (`input/`)
Define the structure of data coming from source systems:
- `850_input_schema.json` - Purchase Order source data format
- `810_input_schema.json` - Invoice source data format
- `270_input_schema.json` - Healthcare Eligibility source format
- `834_input_schema.json` - Benefit Enrollment source format

### Output Schemas (`output/`)
Define the structure of X12 EDI output:
- `850_output_schema.json` - X12 850 format
- `810_output_schema.json` - X12 810 format
- `270_output_schema.json` - X12 270 format
- `834_output_schema.json` - X12 834 format

## Schema Format

All schemas use JSON Schema Draft 7 format.

### Example Input Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "X12 850 Purchase Order Input",
  "type": "object",
  "properties": {
    "purchase_order_number": {
      "type": "string",
      "description": "Unique PO number",
      "minLength": 1,
      "maxLength": 12
    },
    "order_date": {
      "type": "string",
      "format": "date",
      "description": "Date PO was created"
    },
    "supplier_id": {
      "type": "string",
      "maxLength": 10
    },
    "line_items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "item_number": { "type": "string" },
          "quantity": { "type": "number", "minimum": 0 },
          "unit_price": { "type": "number", "minimum": 0 }
        },
        "required": ["item_number", "quantity"]
      }
    }
  },
  "required": ["purchase_order_number", "order_date", "supplier_id"]
}
```

### Example Output Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "X12 850 EDI Format",
  "type": "object",
  "properties": {
    "ISA": {
      "type": "string",
      "description": "Interchange Control Header",
      "pattern": "^ISA\\*.*"
    },
    "GS": {
      "type": "string",
      "description": "Functional Group Header",
      "pattern": "^GS\\*.*"
    },
    "ST": {
      "type": "string",
      "description": "Transaction Set Header",
      "pattern": "^ST\\*.*"
    }
  }
}
```

## Validation Rules

Schemas include:
- **Type** - Data type (string, number, object, array, etc.)
- **Format** - Date, email, URI, etc.
- **Pattern** - Regular expression validation
- **Min/Max** - Length or numeric bounds
- **Required** - Mandatory fields
- **Enum** - Allowed values
- **Description** - Field documentation

## Using Schemas

### In Python
```python
import json
import jsonschema

# Load schema
with open('data/schemas/input/850_input_schema.json') as f:
    schema = json.load(f)

# Validate data
data = {...}
jsonschema.validate(data, schema)
```

### In Tests
```python
from src.validators import SchemaValidator

validator = SchemaValidator()
result = validator.validate(
    data=data,
    schema_file='data/schemas/input/850_input_schema.json'
)
```

## Best Practices

1. **Keep schemas aligned** - Input and output schemas should be consistent
2. **Document fields** - Include descriptions for all properties
3. **Use examples** - Include example data in comments
4. **Version schemas** - Track schema changes
5. **Validate strictly** - Use appropriate validation rules
6. **Test coverage** - Have test data for all schemas

## Adding New Schemas

When adding a schema:
1. Create in appropriate directory (input/ or output/)
2. Use JSON Schema Draft 7 format
3. Include detailed descriptions
4. Add example data
5. Create corresponding test data
6. Update this README
7. Add validation tests

## References

- [JSON Schema Documentation](https://json-schema.org/)
- [X12 Standard Documentation](https://www.x12.org/)
- [Seeburger Documentation](https://www.seeburger.com/)

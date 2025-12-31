# Sample X12 850 Purchase Order

This directory contains sample X12 850 (Purchase Order) EDI documents for testing the Mapping Analyzer.

## Files

- `sample_850_001.edi` - Basic purchase order
- `sample_850_002.edi` - Complex purchase order with multiple line items

## Usage

These files are used by the test suite to:
- Test map analysis capabilities
- Validate against X12 850 standard
- Test code generation for field additions
- Validate input/output schemas

## X12 850 Structure

### Common Segments

| Segment | Description |
|---------|------------|
| ISA | Interchange Control Header |
| GS | Functional Group Header |
| ST | Transaction Set Header |
| BEG | Beginning Segment for Purchase Order |
| REF | Reference Information |
| N1 | Party Identification |
| N2 | Additional Name Information |
| N3 | Address Information |
| N4 | Geographic Location |
| PO1 | Baseline Item Data (Line Item) |
| CTT | Transaction Totals |
| SE | Transaction Set Trailer |
| GE | Functional Group Trailer |
| IEA | Interchange Control Trailer |

## Sample Content

```
ISA*00*          *00*          *02*SENDER         *02*RECEIVER       *210101*120000*U*00401*000000001*0*P*:
GS*PO*SENDER*RECEIVER*20210101*120000*1*X*004010
ST*850*0001
BEG*00*SA*PON123*20210101
REF*CT*CONTRACT123
N1*BY*BUYER_NAME
N1*SU*SUPPLIER_NAME
PO1*1*100*EA*10.00*UP*MFG*ITEM123
PO1*2*50*CS*20.00*UP*MFG*ITEM456
CTT*2
SE*10*0001
GE*1*1
IEA*1*000000001
```

## Field Reference

For detailed X12 850 specifications, see:
- ANSI X12 Standard Documentation
- Trading partner agreements
- Seeburger documentation

## Adding New Test Files

When adding new test files:
1. Follow X12 850 standard format
2. Include sufficient test data for validation
3. Test various scenarios (basic, complex, edge cases)
4. Update this README with description
5. Add corresponding schema files

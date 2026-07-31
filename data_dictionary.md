# Data Dictionary - Mutual Fund Analytics Project

## Table: `fact_nav`
- **amfi_code** (INTEGER): Unique identifier for the mutual fund scheme.
- **scheme_name** (TEXT): Official name of the scheme.
- **nav_date** (DATE): Date for which NAV is calculated.
- **nav** (FLOAT): Net Asset Value per unit on that date.

## Table: `fact_transactions`
- **transaction_id** (INTEGER): Unique ID for each transaction record.
- **investor_name** (TEXT): Name or account identifier of the investor.
- **amount** (FLOAT): Monetary value of the transaction.
- **transaction_type** (TEXT): Type of investment action (`SIP`, `Lumpsum`, `Redemption`).
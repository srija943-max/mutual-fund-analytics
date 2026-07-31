-- Star Schema Definition for Mutual Fund Analytics

CREATE TABLE IF NOT EXISTS dim_fund (
    fund_id INTEGER PRIMARY KEY,
    fund_name TEXT,
    category TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id TEXT PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE IF NOT EXISTS fact_nav (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    scheme_name TEXT,
    nav_date TEXT,
    nav REAL,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(fund_id)
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_name TEXT,
    amount REAL,
    transaction_type TEXT
);
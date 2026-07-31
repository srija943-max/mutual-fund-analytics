-- Analytical SQL Queries

-- 1. Top Transactions by Amount
SELECT * FROM fact_transactions ORDER BY amount DESC LIMIT 5;

-- 2. Transaction Breakdown (SIP vs Lumpsum vs Redemption)
SELECT transaction_type, COUNT(*) as count, SUM(amount) as total_amount 
FROM fact_transactions 
GROUP BY transaction_type;

-- 3. Average NAV Value across all dates
SELECT AVG(nav) as average_nav FROM fact_nav;

-- 4. Highest NAV per scheme
SELECT amfi_code, MAX(nav) as max_nav 
FROM fact_nav 
GROUP BY amfi_code;

-- 5. Total Investments overall
SELECT SUM(amount) as total_invested FROM fact_transactions;
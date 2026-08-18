-- 10 SQL Validation Queries
SELECT COUNT(*) AS total_companies FROM companies;
PRAGMA foreign_key_check;
SELECT sector, COUNT(*) FROM companies GROUP BY sector;
SELECT AVG(opm_percent) FROM profitandloss WHERE fiscal_year = 2024;

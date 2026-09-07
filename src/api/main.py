from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI(title="N100 Financial Intelligence Platform API", version="1.0.0")

def get_db():
    conn = sqlite3.connect("nifty100.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/api/v1/health")
def health():
    return {"status": "ok", "version": "1.0.0", "database": "connected"}

@app.get("/api/v1/companies")
def get_companies():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT company_id, ticker, company_name, sector FROM companies")
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"count": len(rows), "data": rows}

@app.get("/api/v1/companies/{ticker}")
def get_company(ticker: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM companies WHERE ticker = ?", (ticker,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Company not found")
    return dict(row)

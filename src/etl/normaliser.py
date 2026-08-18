def normalize_ticker(ticker: str) -> str:
    return ticker.strip().upper() if ticker else ""

def normalize_year(year_str: str) -> int:
    return int(str(year_str).replace("FY", "").strip()[:4])

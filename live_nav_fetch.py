import requests
import json
import os

schemes = {
    "HDFC Top 100 Direct": "125497",
    "SBI Bluechip": "119551",
    "ICICI Bluechip": "120503",
    "Nippon Large Cap": "118632",
    "Axis Bluechip": "119092"
}

nav_data = {}

for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        nav_data[scheme_name] = {
            "scheme_code": scheme_code,
            "house": data.get('meta', {}).get('fund_house'),
            "latest_nav": data.get('data', [])[0] if data.get('data') else None
        }
        print(f"Fetched NAV for: {scheme_name}")

raw_dir = os.path.join('data', 'raw')
os.makedirs(raw_dir, exist_ok=True)
output_file = os.path.join(raw_dir, 'live_nav.json')

with open(output_file, 'w') as f:
    json.dump(nav_data, f, indent=4)

print(f"\nAll NAV data saved successfully in {output_file}!")
import hashlib
import time
import random
import requests
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# ==========================================
# TELEGRAM BOT CONFIGURATION
# ==========================================
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"  # e.g., "123456789:ABCdefGHI..."
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID_HERE"      # e.g., "987654321"

def send_telegram_sms(message_text):
    if TELEGRAM_BOT_TOKEN != "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message_text, "parse_mode": "Markdown"}
            requests.post(url, json=payload, timeout=3)
        except Exception as e:
            print(f"Telegram Dispatch Error: {e}")

# System State Variables
shipment_id = "SHP-VACCINE-9082"
shipment_status = "In Transit — Nominal"
current_temp = 4.2       # Target Band: 2°C to 8°C
current_humidity = 45.0  
current_shock = 0.02     
driver_location = "Vijayawada Highway, AP"

# Cold-Storage Depots Database with Google Maps Routes
COLD_DEPOTS = [
    {
        "name": "AP Pharma Hub Cold Depot", 
        "distance": "2.4 km", 
        "address": "NH-16 Highway, Gate 3", 
        "phone": "+91-9876543210",
        "route_url": "https://www.google.com/maps/dir/?api=1&destination=16.5062,80.6480"
    },
    {
        "name": "BioLogistics Storage Facility", 
        "distance": "6.1 km", 
        "address": "Sector 5, Industrial Park", 
        "phone": "+91-9123456789",
        "route_url": "https://www.google.com/maps/dir/?api=1&destination=16.5150,80.6320"
    }
]

audit_log = []
previous_hash = "00000000000000000000000000000000"
alert_sent_flag = False

def add_audit_log(event_type, details):
    global previous_hash
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    raw_data = f"{shipment_id}{event_type}{details}{timestamp}{previous_hash}"
    current_hash = hashlib.sha256(raw_data.encode()).hexdigest()
    
    log_entry = {
        "log_id": f"LOG-{len(audit_log) + 1}",
        "shipment_id": shipment_id,
        "event_type": event_type,
        "timestamp": timestamp,
        "hash": current_hash[:16] + "...",
        "prev_hash": previous_hash[:16] + "..."
    }
    audit_log.append(log_entry)
    previous_hash = current_hash

add_audit_log("SHIPMENT_REGISTERED", "Vaccine batch loaded with 2°C - 8°C band")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Autonomous Cold-Chain Integrity Platform</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }
        .container { max-width: 1100px; margin: auto; }
        h1 { text-align: center; color: #38bdf8; margin-bottom: 5px; }
        .subtitle { text-align: center; color: #94a3b8; font-size: 14px; margin-bottom: 25px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .card { background: #1e293b; border: 1px solid #334155; padding: 20px; border-radius: 10px; }
        .status-badge { display: inline-block; padding: 6px 12px; border-radius: 20px; font-weight: bold; }
        .status-nominal { background: #065f46; color: #34d399; }
        .status-risk { background: #991b1b; color: #fca5a5; }
        .alert-card { background: #450a0a; border: 2px solid #ef4444; display: none; margin-top: 20px; padding: 20px; border-radius: 10px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 12px; }
        th, td { border: 1px solid #334155; padding: 8px; text-align: left; }
        th { background: #0f172a; color: #38bdf8; }
        .metric-val { font-size: 24px; font-weight: bold; color: #38bdf8; }
        .route-btn { display: inline-block; background: #2563eb; color: white; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 10px; }
        .route-btn:hover { background: #1d4ed8; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚛 Autonomous Cold-Chain Integrity & Rerouting Platform</h1>
        <div class="subtitle">Real-Time Telemetry • 30-60 Min AI Breach Forecasting • Auto Rerouting & Driver SMS</div>

        <div class="card" style="margin-bottom: 20px;">
            <h3>Shipment Monitoring Pipeline</h3>
            <p><strong>Shipment ID:</strong> <span id="shp-id">--</span> | <strong>Status:</strong> <span id="status-badge" class="status-badge status-nominal">--</span></p>
            <p><strong>Current Vehicle Location:</strong> <span id="gps">--</span></p>
        </div>

        <div class="grid">
            <div class="card">
                <h3>Edge Telemetry Data</h3>
                <p>Temperature: <span class="metric-val" id="temp">--</span> °C (Safe: 2°C - 8°C)</p>
                <p>Humidity: <span class="metric-val" id="hum">--</span> %</p>
                <p>Shock Force: <span class="metric-val" id="shock">--</span> g</p>
            </div>

            <div class="card">
                <h3>Predictive Risk Forecasting</h3>
                <p>Breach Risk Score: <span class="metric-val" id="risk-score">0%</span></p>
                <p>Trajectory Forecast: <span id="forecast-txt" style="color: #34d399;">Nominal condition expected.</span></p>
            </div>
        </div>

        <div class="alert-card" id="alert-box">
            <h2 style="color: #f87171; margin-top: 0;">🚨 CRITICAL BREACH FORECAST & DRIVER SMS DISPATCHED</h2>
            <p id="alert-msg"></p>
            <hr style="border-color: #7f1d1d;">
            <h3>📍 Assigned Nearest Cold Storage Depot & Navigation Route</h3>
            <p><strong>Depot Name:</strong> <span id="depot-name">--</span></p>
            <p><strong>Distance:</strong> <span id="depot-dist">--</span></p>
            <p><strong>Address:</strong> <span id="depot-addr">--</span></p>
            <p><strong>Contact Phone:</strong> <span id="depot-phone">--</span></p>
            <a id="route-link" href="#" target="_blank" class="route-btn">🗺️ Open GPS Navigation Route to Depot</a>
        </div>

        <div class="card" style="margin-top: 20px;">
            <h3>Hash-Chained Compliance Audit Log</h3>
            <table>
                <thead>
                    <tr>
                        <th>Log ID</th>
                        <th>Event Type</th>
                        <th>Timestamp</th>
                        <th>Current Hash SHA256</th>
                        <th>Prev Hash</th>
                    </tr>
                </thead>
                <tbody id="audit-table"></tbody>
            </table>
        </div>
    </div>

    <script>
        function updateDashboard() {
            fetch('/stream')
                .then(res => res.json())
                .then(data => {
                    document.getElementById('shp-id').innerText = data.shipment_id;
                    document.getElementById('gps').innerText = data.gps;
                    document.getElementById('temp').innerText = data.temp;
                    document.getElementById('hum').innerText = data.humidity;
                    document.getElementById('shock').innerText = data.shock;
                    document.getElementById('risk-score').innerText = data.risk_score + '%';
                    document.getElementById('forecast-txt').innerText = data.forecast;

                    const statusBadge = document.getElementById('status-badge');
                    statusBadge.innerText = data.status;

                    const alertBox = document.getElementById('alert-box');
                    if (data.is_risk) {
                        statusBadge.className = 'status-badge status-risk';
                        alertBox.style.display = 'block';
                        document.getElementById('alert-msg').innerText = data.alert_message;
                        document.getElementById('depot-name').innerText = data.depot.name;
                        document.getElementById('depot-dist').innerText = data.depot.distance;
                        document.getElementById('depot-addr').innerText = data.depot.address;
                        document.getElementById('depot-phone').innerText = data.depot.phone;
                        document.getElementById('route-link').href = data.depot.route_url;
                    } else {
                        statusBadge.className = 'status-badge status-nominal';
                        alertBox.style.display = 'none';
                    }

                    let rows = '';
                    data.audit_logs.slice().reverse().forEach(log => {
                        rows += `<tr>
                            <td>${log.log_id}</td>
                            <td>${log.event_type}</td>
                            <td>${log.timestamp}</td>
                            <td>${log.hash}</td>
                            <td>${log.prev_hash}</td>
                        </tr>`;
                    });
                    document.getElementById('audit-table').innerHTML = rows;
                });
        }

        setInterval(updateDashboard, 3000);
        window.onload = updateDashboard;
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/stream')
def stream_telemetry():
    global current_temp, shipment_status, alert_sent_flag
    
    current_temp += random.choice([0.3, 0.6, 0.9, 1.4])
    if current_temp > 14.0:
        current_temp = 4.0
        shipment_status = "In Transit — Nominal"
        alert_sent_flag = False
        add_audit_log("STATE_RESET", "Shipment reset to Nominal state")

    humidity = round(current_humidity + random.uniform(-1, 1), 1)
    shock = round(current_shock + random.uniform(0, 0.05), 3)

    risk_score = 0
    is_risk = False
    forecast_txt = "Nominal trajectory. Temperature remains within safe band (2°C - 8°C)."
    alert_msg = ""
    selected_depot = {"name": "--", "distance": "--", "address": "--", "phone": "--", "route_url": "#"}

    if current_temp > 6.5 and current_temp <= 8.0:
        risk_score = 65
        shipment_status = "Risk Detected"
        forecast_txt = "WARNING: Temperature rising! Breach predicted in ~40 minutes."

    elif current_temp > 8.0:
        risk_score = 98
        is_risk = True
        shipment_status = "Rerouting — Auto-Optimized"
        forecast_txt = "CRITICAL BREACH IMMINENT! Temperature exceeding safe limit (8°C)."
        selected_depot = COLD_DEPOTS[0]
        alert_msg = f"Temperature reached {current_temp:.1f}°C. Cargo risk CRITICAL! System auto-rerouted driver to nearest cold storage."
        
        # Dispatch SMS Alert once per breach cycle
        if not alert_sent_flag:
            sms_text = (
                f"🚨 *CRITICAL COLD-CHAIN ALERT*\n\n"
                f"Shipment: {shipment_id}\n"
                f"Current Temp: {current_temp:.1f}°C (Exceeded 8.0°C)\n"
                f"Risk Score: 98%\n\n"
                f"📍 *REROUTE LOCATION:*\n"
                f"Depot: {selected_depot['name']}\n"
                f"Distance: {selected_depot['distance']}\n"
                f"Address: {selected_depot['address']}\n"
                f"Contact: {selected_depot['phone']}\n\n"
                f"🗺️ *NAVIGATION ROUTE:*\n"
                f"{selected_depot['route_url']}"
            )
            send_telegram_sms(sms_text)
            add_audit_log("DRIVER_SMS_SENT", f"Telegram Alert & Route dispatched for {selected_depot['name']}")
            alert_sent_flag = True

    return jsonify({
        "shipment_id": shipment_id,
        "status": shipment_status,
        "gps": driver_location,
        "temp": round(current_temp, 1),
        "humidity": humidity,
        "shock": shock,
        "risk_score": risk_score,
        "forecast": forecast_txt,
        "is_risk": is_risk,
        "alert_message": alert_msg,
        "depot": selected_depot,
        "audit_logs": audit_log
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
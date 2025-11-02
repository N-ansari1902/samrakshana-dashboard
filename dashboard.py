import streamlit as st
import pandas as pd
import requests
import time

API_URL = st.sidebar.text_input("🌐 API Base URL", "http://127.0.0.1:5000")

st.title("📊 SAMRAKSHANA Cloud Dashboard (v2)")
st.write("Live IoT Device Monitoring and Anomaly Alerts")

# Get registered devices
def get_devices():
    try:
        res = requests.get(f"{API_URL}/devices", timeout=5)
        return res.json()
    except Exception:
        return []

# Get latest data for device
def get_latest(device_id):
    try:
        res = requests.get(f"{API_URL}/latest/{device_id}", timeout=5)
        return res.json()
    except Exception:
        return []

# Refresh rate
interval = st.sidebar.slider("⏱ Refresh interval (seconds)", 5, 60, 10)

while True:
    devices = get_devices()
    if not devices:
        st.warning("⚠️ No devices registered yet.")
        time.sleep(interval)
        st.experimental_rerun()

    for d in devices:
        device_id = d["device_id"]
        st.subheader(f"Device: {device_id}")

        data = get_latest(device_id)
        if not data:
            st.info("No sensor data available yet.")
            continue

        df = pd.DataFrame(data)
        df["time"] = pd.to_datetime(df["ts"], unit="s")

        st.line_chart(df.set_index("time")[["temperature", "humidity"]])

    time.sleep(interval)
    st.experimental_rerun()

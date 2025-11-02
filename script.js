// script.js
const API_BASE = "https://samrakshana-backend.azurewebsites.net";

async function loadLatest() {
    const deviceId = document.getElementById("deviceId").value;
    if(!deviceId) return;

    const res = await fetch(`${API_BASE}/latest/${deviceId}`);
    const data = await res.json();
    console.log(data);

    const out = document.getElementById("output");
    out.innerText = JSON.stringify(data, null, 2);
}

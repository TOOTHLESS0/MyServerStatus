from flask import Flask, jsonify, send_from_directory
from mcstatus import JavaServer
from pathlib import Path
import time

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)

MC_HOST = "127.0.0.1"
MC_PORT = 25555


@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/logo.png")
def logo():
    return send_from_directory(BASE_DIR, "logo.png")


@app.get("/api/status")
def status():
    checked_at = int(time.time())

    try:
        server = JavaServer(MC_HOST, MC_PORT, timeout=2.5)
        result = server.status()

        try:
            motd = result.motd.to_plain()
        except Exception:
            motd = str(result.motd)

        return jsonify({
            "online": True,
            "players_online": result.players.online,
            "players_max": result.players.max,
            "version": result.version.name,
            "latency_ms": round(result.latency),
            "motd": motd,
            "checked_at": checked_at
        }), 200

    except Exception:
        return jsonify({
            "online": False,
            "players_online": 0,
            "players_max": None,
            "version": None,
            "latency_ms": None,
            "motd": None,
            "checked_at": checked_at
        }), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)

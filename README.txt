MINECRAFT SERVER STATUS PAGE (Windows)

This status page is configured for the Minecraft Java server you previously described as listening on port 25555 on this same PC.

1. Install Python 3 from https://www.python.org/downloads/windows/ if `py` is not recognized.
2. Keep your Minecraft server running.
3. Double-click start-status-site.bat. The first run installs Flask and mcstatus.
4. Open http://127.0.0.1:8080 in your browser. Check that status and player count work locally.
5. Install cloudflared from the official guide: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/
6. Open a SECOND Command Prompt and run:
   cloudflared tunnel --url http://localhost:8080
7. Open the https://....trycloudflare.com URL printed in that window. Share it to let others view the status page.

IMPORTANT:
- Keep both the status app and cloudflared running; keep the PC awake and online.
- Quick Tunnel addresses are temporary and can change after restart.
- No Minecraft port forwarding is required for this status page because the checker queries the server locally.
- This is a read-only status page. It does not provide server controls.
- If the Minecraft server's port has changed, edit MC_PORT in app.py.
- If the server runs on another computer, change MC_HOST in app.py to that computer's LAN IP, and ensure local firewall rules allow the status PC to reach its Minecraft port.

# KodiProtonVPNMediaStreamingAutomator

Automatically launch Kodi with ProtonVPN connected then disconnect VPN when Kodi closes.

## Features

- Auto-connects to ProtonVPN when you launch Kodi
- Auto-disconnects VPN when Kodi is closed
- All-in-one `.exe` — no Python required!

## Download

Grab the `.exe` from the [Releases](https://github.com/CameronSharp9402/KodiVPNLauncher/releases) page.

## Requirements

- **Kodi** installed at: `C:\Program Files\Kodi\kodi.exe`
- **ProtonVPN** installed at: `C:\Program Files\Proton\VPN\ProtonVPN.Launcher.exe`
- ProtonVPN must have **Auto-Connect** enabled
- Run `.exe` as Administrator to allow VPN disconnect

## Optional for Developers

If you'd rather run the Python script:

```bash
pip install -r requirements.txt
python kodi_vpn_launcher.py


# KodiProtonVPNMediaStreamingAutomator

A simple automation script that launches **Kodi** and automatically connects to **ProtonVPN**, then disconnects when Kodi closes.

## Features

- Launches ProtonVPN (auto-connect must be enabled)
- Starts Kodi
- Automatically kills ProtonVPN when Kodi exits

## Requirements

- Python 3.10+
- `psutil` module: `pip install psutil`
- ProtonVPN installed with auto-connect enabled
- ***Optional, make sure the kill switch in enabled***

## Usage

1. Install dependencies
2. Run `kodi_vpn_launcher.py`
3. Build `.exe` with:  
   ```bash
   pyinstaller --onefile KodiVPNMediaStreamingAutomation.py

# KodiVPNLauncher

**KodiVPNLauncher** is a lightweight Windows utility that automatically:

- Launches **ProtonVPN** and connects using its auto-connect setting  
- Starts **Kodi**  
- Disconnects VPN and kills ProtonVPN when Kodi is closed  
- Ensures VPN and Kodi are also closed if the launcher is force-quit

---

## Requirements

- **Windows 10 or 11**
- **ProtonVPN** installed at:  
  `C:\Program Files\Proton\VPN\ProtonVPN.Launcher.exe`
- **Kodi** installed at:  
  `C:\Program Files\Kodi\kodi.exe`
- ProtonVPN must have **Auto-Connect on Launch** enabled in its settings
- Script requires **Administrator rights** to kill background services
- ***Optional, enable "Kill-switch" in ProtonVPN***

---

## How to Use (Python Users)

1. Clone or download this repository
2. (Optional) Create a virtual environment
3. Run the launcher:
   ```bash
   python KodiVPNMediaStreamingAutomation.py
   ```

> If `psutil` is not installed, the script will attempt to install it automatically.
>  If the script fails to auto-install `psutil`, you can install it manually:
>
> ```bash
> pip install psutil
> ```


---

## Prebuilt Executable

To skip installing Python, download the `.exe` from the [Releases](https://github.com/CameronSharp9402/KodiVPNLauncher/releases) page and:

- **Right-click > Run as administrator**
- Kodi will launch with VPN connected
- When Kodi exits, ProtonVPN will disconnect automatically

---

## Exit Behavior

The launcher handles:

- Kodi closing normally
- User pressing `CTRL+C`
- Force-closing the terminal window

In all cases, it will attempt to clean up by killing ProtonVPN and Kodi.

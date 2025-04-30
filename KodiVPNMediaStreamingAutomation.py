import subprocess
import time
import os
import signal
import atexit
try:
    import psutil
except ImportError:
    import subprocess
    import sys
    print("[*] psutil not found. Installing it now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    import psutil


# Make sure these match your file locations otherwise the script will throw an error!
kodi_path = r"C:\Program Files\Kodi\kodi.exe"
protonvpn_path = r"C:\Program Files\Proton\VPN\ProtonVPN.Launcher.exe"

def launch_protonvpn():
    print("[+] Launching ProtonVPN...")
    subprocess.Popen([protonvpn_path])
    time.sleep(10)  # Let ProtonVPN open

def wait_for_user_to_connect():
    input("[*] Connect to a VPN in ProtonVPN and press ENTER to continue...")

def launch_kodi():
    print("[+] Launching Kodi...")
    kodi_process = subprocess.Popen([kodi_path])
    return kodi_process

def wait_for_kodi_close(process):
    print("[*] Waiting for Kodi to close...")
    process.wait()
    print("[+] Kodi closed.")

def kill_protonvpn():
    print("[*] Killing ProtonVPN-related processes...")
    vpn_processes = [
        "ProtonVPN.WireGuardService.exe",
        "ProtonVPNService.exe",
        "ProtonVPN.Client.exe"
    ]

    found_any = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] in vpn_processes:
                os.system(f"taskkill /PID {proc.info['pid']} /F")
                print(f"[+] Killed {proc.info['name']} (PID: {proc.info['pid']})")
                found_any = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not found_any:
        print("[-] No ProtonVPN processes found.")

def kill_kodi():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if 'kodi.exe' in proc.info['name'].lower():
                os.system(f"taskkill /PID {proc.info['pid']} /F")
                print(f"[+] Killed Kodi (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def cleanup(*args):
    print("[!] Cleanup triggered. Killing Kodi and ProtonVPN...")
    kill_kodi()
    kill_protonvpn()
    print("[✓] Cleaned up.")
    exit(0)

def main():
    # Register cleanup so it's triggered if user hits Ctrl+C during launch
    signal.signal(signal.SIGINT, cleanup)   # CTRL+C
    signal.signal(signal.SIGTERM, cleanup)  # Termination
    atexit.register(cleanup)                # Normal exit

    launch_protonvpn()
    wait_for_user_to_connect()
    kodi = launch_kodi()
    wait_for_kodi_close(kodi)
    kill_protonvpn()

    print("[✓] Done.")

if __name__ == "__main__":
    main()

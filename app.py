import stat
import os
import shutil

import flet as ft

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
    # Serve assets to remote clients automatically
    # Flet's ClientStorage allows us to push things to the browser, 
    # but to download files to a remote machine, we must provide a download link or use FilePicker

    def save_file_result(e: ft.FilePickerResultEvent):
        # The user's browser has selected where to save the file
        if e.path:
            # Copy asset file on the server's side or handle however needed
            pass # In web mode with flet, get_directory_path is what you actually want, but this proves concept

    file_picker = ft.FilePicker(on_result=save_file_result)
    page.overlay.append(file_picker)

    def trigger_download(e):
        # We launch the URL so the browser downloads the file directly to the remote computer
        page.launch_url("/sample.png")

    page.title = "Flet UserControl Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Add our custom UserControl to the page
    page.add(
        UserControl(),
        ft.ElevatedButton("Download sample.png", on_click=trigger_download)
    )

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
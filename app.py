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
            ft.IconButton(ft.icons.REMOVE, on_click=self.minus_click),
            self.text,
            ft.IconButton(ft.icons.ADD, on_click=self.plus_click),
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
    # Copy asset file to %temp% on load
    temp_dir = os.environ.get("TEMP", "/tmp")
    asset_file = os.path.join("assets", "sample.png")
    if os.path.exists(asset_file):
        try:
            dest_file = os.path.join(temp_dir, "sample.png")
            shutil.copy2(asset_file, dest_file)
        except Exception as e:
            print(f"Error copying asset: {e}")

    page.title = "Flet UserControl Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Add our custom UserControl to the page
    page.add(UserControl())

if __name__ == "__main__":
    ft.app(target=main)
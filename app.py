import flet as ft

class UserControl(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def build(self):
        self.text = ft.Text(str(self.counter), size=20)
        return ft.Row([
            ft.IconButton(ft.icons.REMOVE, on_click=self.minus_click),
            self.text,
            ft.IconButton(ft.icons.ADD, on_click=self.plus_click),
        ])

    def minus_click(self, e):
        self.counter -= 1
        self.text.value = str(self.counter)
        self.update()

    def plus_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

def main(page: ft.Page):
    page.title = "Flet UserControl Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Add our custom UserControl to the page
    page.add(UserControl())

if __name__ == "__main__":
    ft.app(target=main)
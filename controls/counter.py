import flet as ft


class CounterControl(ft.Column):
    """Reusable counter control that demonstrates UserControl-style UI modularity.

    Each instance maintains its own independent state (current value), making
    it safe to place multiple counters on the same page.

    Args:
        label: Display label shown above the counter.
        initial_value: Starting numeric value (defaults to 0).
    """

    def __init__(self, label: str = "Counter", initial_value: int = 0, **kwargs):
        super().__init__(**kwargs)
        self._label = label
        self._initial_value = initial_value
        self._value = initial_value
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self._count_text = ft.Text(
            str(self._value),
            size=32,
            weight=ft.FontWeight.BOLD,
        )

        self.controls = [
            ft.Text(self._label, size=16, color=ft.Colors.BLUE_GREY_700),
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.REMOVE,
                        on_click=self._decrement,
                        tooltip="Decrement",
                    ),
                    self._count_text,
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=self._increment,
                        tooltip="Increment",
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]

    @property
    def value(self) -> int:
        """Current counter value."""
        return self._value

    def _increment(self, e: ft.ControlEvent) -> None:
        self._value += 1
        self._count_text.value = str(self._value)
        self.update()

    def _decrement(self, e: ft.ControlEvent) -> None:
        self._value -= 1
        self._count_text.value = str(self._value)
        self.update()

    def reset(self) -> None:
        """Reset the counter back to its initial value."""
        self._value = self._initial_value
        self._count_text.value = str(self._initial_value)
        self.update()

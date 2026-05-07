from __future__ import annotations

from typing import Callable, Optional

import flet as ft


class TaskItem(ft.Row):
    """Reusable task-item control with completion toggle and delete button.

    Encapsulates all the state and behaviour for a single task entry so the
    parent only needs to supply a name and an optional delete callback.

    Args:
        task_name: The text label displayed for this task.
        on_delete: Optional callable that receives this ``TaskItem`` instance
            when the delete button is pressed.
    """

    def __init__(
        self,
        task_name: str,
        on_delete: Optional[Callable[[TaskItem], None]] = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._task_name = task_name
        self._on_delete_callback = on_delete
        self._completed = False

        self._checkbox = ft.Checkbox(
            label=self._task_name,
            value=False,
            on_change=self._toggle_completion,
        )
        self._delete_btn = ft.IconButton(
            icon=ft.Icons.DELETE_OUTLINE,
            icon_color=ft.Colors.RED_400,
            on_click=self._handle_delete,
            tooltip="Delete task",
        )

        self.controls = [
            self._checkbox,
            ft.Container(expand=True),
            self._delete_btn,
        ]
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

    @property
    def task_name(self) -> str:
        """The name of this task."""
        return self._task_name

    @property
    def completed(self) -> bool:
        """Whether this task has been marked as complete."""
        return self._completed

    def _toggle_completion(self, e: ft.ControlEvent) -> None:
        self._completed = e.control.value
        self._checkbox.label_style = ft.TextStyle(
            decoration=ft.TextDecoration.LINE_THROUGH if self._completed else None,
            color=ft.Colors.GREY_500 if self._completed else None,
        )
        self.update()

    def _handle_delete(self, e: ft.ControlEvent) -> None:
        if self._on_delete_callback:
            self._on_delete_callback(self)

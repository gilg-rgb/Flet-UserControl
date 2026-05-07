import flet as ft

from controls import CounterControl, TaskItem


def main(page: ft.Page) -> None:
    page.title = "Flet UserControl Demo"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # ------------------------------------------------------------------
    # Counter section — two independent CounterControl instances
    # ------------------------------------------------------------------
    counter1 = CounterControl(label="Score", initial_value=0)
    counter2 = CounterControl(label="Lives", initial_value=3)

    def reset_counters(e: ft.ControlEvent) -> None:
        counter1.reset()
        counter2.reset()

    counter_section = ft.Card(
        content=ft.Container(
            padding=16,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Counter Controls",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Two independent CounterControl instances sharing no state.",
                        color=ft.Colors.GREY_600,
                    ),
                    ft.Divider(),
                    ft.Row(
                        controls=[counter1, counter2],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    ft.ElevatedButton("Reset All", on_click=reset_counters),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
    )

    # ------------------------------------------------------------------
    # Task-list section — dynamically created TaskItem instances
    # ------------------------------------------------------------------
    task_list = ft.Column(controls=[], spacing=4)

    def _add_task(e: ft.ControlEvent) -> None:
        name = task_input.value.strip()
        if not name:
            return
        item = TaskItem(task_name=name, on_delete=_delete_task)
        task_list.controls.append(item)
        task_input.value = ""
        page.update()

    def _delete_task(item: TaskItem) -> None:
        task_list.controls.remove(item)
        page.update()

    task_input = ft.TextField(
        label="New task",
        expand=True,
        on_submit=_add_task,
    )

    task_section = ft.Card(
        content=ft.Container(
            padding=16,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Task List",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Each row is a reusable TaskItem with its own completion state.",
                        color=ft.Colors.GREY_600,
                    ),
                    ft.Divider(),
                    ft.Row(
                        controls=[
                            task_input,
                            ft.ElevatedButton("Add", on_click=_add_task),
                        ]
                    ),
                    task_list,
                ]
            ),
        )
    )

    page.add(
        ft.Text(
            "Flet UserControl Demo",
            size=28,
            weight=ft.FontWeight.BOLD,
        ),
        ft.Text(
            "Reusable UI components for better modularity.",
            color=ft.Colors.GREY_600,
        ),
        ft.Divider(),
        counter_section,
        task_section,
    )


ft.app(target=main)

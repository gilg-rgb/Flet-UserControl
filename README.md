# Flet-UserControl

A demonstration of reusable UI components in [Flet](https://flet.dev/), the Python framework for building cross-platform apps.

## What is a UserControl?

A *UserControl* is a self-contained, reusable UI component that encapsulates its own state and behaviour.  
Each instance manages its own data so it can be placed on a page multiple times without components interfering with each other.

This project ships two example controls:

| Control | File | Description |
|---------|------|-------------|
| `CounterControl` | `controls/counter.py` | Increment / decrement counter with independent state |
| `TaskItem` | `controls/task_item.py` | Single task row with completion toggle and delete |

Both are used together in `main.py` to build a small demo app.

## Project structure

```
Flet-UserControl/
├── controls/
│   ├── __init__.py       # Package exports
│   ├── counter.py        # CounterControl component
│   └── task_item.py      # TaskItem component
├── main.py               # Demo app entry-point
├── requirements.txt
└── README.md
```

## Getting started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the demo

```bash
python main.py
```

A native window (or browser tab) will open showing:

- **Counter Controls** — two `CounterControl` instances with independent counts and a shared *Reset All* button.
- **Task List** — add tasks by typing and pressing **Add** or Enter; tick the checkbox to mark a task complete; click the bin icon to remove it.

## Creating your own UserControl

Subclass `ft.Column`, `ft.Row`, or `ft.Container`, build the control tree in `__init__`, and call `self.update()` after any state change:

```python
import flet as ft

class GreetingCard(ft.Column):
    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self._name = name
        self._greeting = ft.Text(f"Hello, {name}!")
        self.controls = [
            self._greeting,
            ft.ElevatedButton("Wave", on_click=self._wave),
        ]

    def _wave(self, e: ft.ControlEvent) -> None:
        self._greeting.value = f"👋 Hi, {self._name}!"
        self.update()
```

## License

[MIT](LICENSE)

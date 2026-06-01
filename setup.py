from setuptools import setup, find_packages

setup(
    name="flet-usercontrol",
    version="0.1.0",
    description="Flet UserControl Component Library",
    author="Gilg",
    url="https://github.com/gilg-rgb/Flet-UserControl",
    py_modules=["app"],
    install_requires=[
        "flet",
        "requests",
    ],
    python_requires=">=3.7",
)

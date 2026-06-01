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
    def __init__(self, **kwargs):          
        super().__init__(**kwargs)
        self.state = {}
        self.content = self.build()


    def build(self) -> ft.Control:        
        return ft.Text("Base Component - Override build()")

    def set_state(self, **kwargs):        
        self.state.update(kwargs)
        self.content = self.build()
        self.update()

    def setState(self, callback):
        callback()
        self.content = self.build()
        self.update()

    def update(self, callback):
        callback()
        self.content = self.build()
        self.update()

    
    

    

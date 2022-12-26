import sys
from cx_Freeze import setup, Executable
from tkinter import *
import random
import time
from playsound import playsound


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("Bounce_Game.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ['playsound','time','random','tkinter'],
        include_files = ['Jump_sound.wav'],
        include_msvcr = [True],
        add_to_path = [True],
        excludes = []
)




setup(
    name = "Bounce Game",
    version = "1.5.5",
    description = "Bounce Game by Lucas Santana Santos",
    options = dict(build_exe = buildOptions),
    executables = executables
 )

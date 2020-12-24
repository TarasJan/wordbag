import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes": ["tkinter", 'genanki', 'keyboard', 'mouse']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "wordbag",
    version = "0.2.1",
    description = "Wordbag - sentence mining tool for desktop use",
    options = {"build_exe": build_exe_options},
    executables = [Executable("client.py", base = base)])

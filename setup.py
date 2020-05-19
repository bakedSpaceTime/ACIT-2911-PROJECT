"""
Pandemic Run
Course: ACIT 2911, Agile Development
Authors:
- Jaskaran Saini, A01055847
- Jeffery Law, A00864331
- Ming Yen Hsieh, A01170219
- Tushya Iyer, A01023434
- Shivar Pillay, A01079978
- Shivam Patel, A01185250
"""

""" Script to convert our python modules into an executable file for Windows """
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": [], "include_files": ["images", "audio"]}

base = None

setup(
    name = "Pandemic Run",
    url = "https://github.com/bakedSpaceTime/ACIT-2911-PROJECT",
    author = "Jaskaran Saini, Jeffery Law, Ming Yen Hsieh, Tushya Iyer, Shivar Pillay, Shivam Patel",
    version = "0.3",
    description = "Pandemic Run game developed for ACIT 2911 Winter 2020",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base)]   
)

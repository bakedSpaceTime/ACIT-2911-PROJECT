import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": [], "include_files": ["images", "audio"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
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

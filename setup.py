import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages=['pygame'],
    excludes=['tkinter'],
    include_files= ['Assets/', "Scripts/"],
    build_exe= "./bin/build/",
)

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('DinoRunner.py', base=base)
]

setup(name='Dino Runner',
      version= '1.0',
      description= '',
      options= dict(build_exe= buildOptions),
      executables= executables
)

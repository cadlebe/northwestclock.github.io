from cx_Freeze import setup, Executable

setup(name="nwclock",
      version="0.2.0",
      description="Simple clock that displays UTC, date, and temp.",
      executables=[Executable("src/clock.py")])

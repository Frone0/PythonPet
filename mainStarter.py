import os
import traceback

os.system("")  # turns on colors in old Windows consoles

try:
    import PythonPet
    PythonPet.StartZero()
except Exception:
    # When the .exe is double-clicked, the window closes on a crash,
    # so show the error and wait instead
    traceback.print_exc()
    input("Something went wrong. Press Enter to close...")

import time
import ctypes
from ctypes import wintypes
import psutil

user32 = ctypes.windll.user32



def get_fg() -> str:
    h_wnd = user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
    return psutil.Process(pid.value).name()


def main():
    while True:
        time.sleep(1)
        print(get_fg())

        
if __name__ == "__main__":
    main()
    
"""Windows "run at startup" toggle via the HKCU Run registry key.

Only touches the registry on Windows; importing/calling this on any other
OS is a safe no-op so the rest of the app can still be developed/tested
cross-platform.
"""
from __future__ import annotations

import sys

RUN_KEY = r"Software\Microsoft\Windows\CurrentVersion\Run"
VALUE_NAME = "ShamsiCalWidget"


def _exe_path() -> str:
    if getattr(sys, "frozen", False):
        # Running as a PyInstaller-built exe
        return f'"{sys.executable}"'
    # Running from source with `python main.py`
    return f'"{sys.executable}" "{sys.argv[0]}"'


def is_supported() -> bool:
    return sys.platform == "win32"


def is_enabled() -> bool:
    if not is_supported():
        return False
    import winreg

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_KEY, 0, winreg.KEY_READ) as key:
            winreg.QueryValueEx(key, VALUE_NAME)
            return True
    except FileNotFoundError:
        return False


def set_enabled(enabled: bool) -> None:
    if not is_supported():
        return
    import winreg

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_KEY, 0, winreg.KEY_SET_VALUE) as key:
        if enabled:
            winreg.SetValueEx(key, VALUE_NAME, 0, winreg.REG_SZ, _exe_path())
        else:
            try:
                winreg.DeleteValue(key, VALUE_NAME)
            except FileNotFoundError:
                pass

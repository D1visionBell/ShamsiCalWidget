"""Resolve paths to bundled resources (fonts, icon) both when running from
source and when running as a frozen PyInstaller exe (which unpacks data
files into sys._MEIPASS at runtime)."""
from __future__ import annotations

import sys
from pathlib import Path


def resource_path(*parts: str) -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base = Path(sys._MEIPASS)
    else:
        base = Path(__file__).resolve().parent
    return base.joinpath(*parts)


def vazir_font(style: str, point_size: int):
    """Vazirmatn's Bold/Medium weights live under one family ("Vazirmatn")
    as distinct *styles* — there is no separate "Vazirmatn Bold" family."""
    from PySide6.QtGui import QFont

    font = QFont("Vazirmatn")
    font.setStyleName(style)
    font.setPointSize(point_size)
    return font


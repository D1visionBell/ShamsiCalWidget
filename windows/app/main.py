"""ShamsiCalWidget for Windows — entry point.

A frameless, draggable, always-on-top-toggleable floating widget (mirrors
the Android 2x2 home widget), a system tray icon, and a full month-view
calendar window opened on click.
"""
from __future__ import annotations

import sys

from PySide6.QtCore import QTimer
from PySide6.QtGui import QFontDatabase, QIcon
from PySide6.QtWidgets import QApplication

from resources_util import resource_path
from settings_store import Settings
from overlay_widget import OverlayWidget
from calendar_window import CalendarWindow
from tray import TrayIcon


def load_fonts():
    for name in ("vazirmatn_medium.ttf", "vazirmatn_bold.ttf"):
        path = resource_path("resources", "fonts", name)
        QFontDatabase.addApplicationFont(str(path))


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # keep running in the tray

    load_fonts()

    settings = Settings()

    icon_path = resource_path("resources", "icon.ico")
    icon = QIcon(str(icon_path))
    if not icon.isNull():
        app.setWindowIcon(icon)

    overlay = OverlayWidget(settings)
    overlay.show()

    calendar_window: CalendarWindow | None = None

    def open_calendar():
        nonlocal calendar_window
        if calendar_window is None:
            calendar_window = CalendarWindow(settings)
        calendar_window.show()
        calendar_window.raise_()
        calendar_window.activateWindow()

    overlay.open_calendar_requested.connect(open_calendar)
    overlay.exit_requested.connect(app.quit)

    tray = TrayIcon(icon, settings, overlay, open_calendar)
    tray.show()

    # Force a repaint periodically so the widget always reflects the live
    # system date (paintEvent reads jalali.today() fresh every time — no
    # caching, so there's nothing that can go stale between ticks).
    timer = QTimer()
    timer.timeout.connect(overlay.refresh_date)
    timer.start(20_000)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

"""System tray icon: mirrors the overlay widget's right-click menu, plus
show/hide and a "start with Windows" toggle."""
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMenu

import autostart
from settings_store import Settings


class TrayIcon(QSystemTrayIcon):
    def __init__(self, icon: QIcon, settings: Settings, overlay, calendar_opener):
        super().__init__(icon)
        self.settings = settings
        self.overlay = overlay
        self._open_calendar = calendar_opener
        self.setToolTip("تقویم شمسی")

        menu = QMenu()
        menu.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.toggle_widget_action = menu.addAction("نمایش/مخفی کردن ویجت")
        self.toggle_widget_action.triggered.connect(self._toggle_widget_visibility)

        open_action = menu.addAction("باز کردن تقویم")
        open_action.triggered.connect(self._open_calendar)

        menu.addSeparator()

        self.on_top_action = menu.addAction("همیشه روی صفحه")
        self.on_top_action.setCheckable(True)
        self.on_top_action.setChecked(settings.always_on_top)
        self.on_top_action.triggered.connect(self._toggle_on_top)

        self.dark_action = menu.addAction("حالت تیره")
        self.dark_action.setCheckable(True)
        self.dark_action.setChecked(settings.dark_mode)
        self.dark_action.triggered.connect(self._toggle_dark)

        self.autostart_action = menu.addAction("اجرا هنگام روشن شدن ویندوز")
        self.autostart_action.setCheckable(True)
        self.autostart_action.setChecked(settings.autostart)
        self.autostart_action.triggered.connect(self._toggle_autostart)

        menu.addSeparator()
        exit_action = menu.addAction("خروج")
        exit_action.triggered.connect(self._quit)

        self.setContextMenu(menu)
        self.activated.connect(self._on_activated)

    def _toggle_widget_visibility(self):
        self.overlay.setVisible(not self.overlay.isVisible())

    def _toggle_on_top(self):
        self.settings.always_on_top = self.on_top_action.isChecked()
        self.settings.sync()
        self.overlay.apply_on_top_change()

    def _toggle_dark(self):
        self.settings.dark_mode = self.dark_action.isChecked()
        self.settings.sync()
        self.overlay.apply_theme_change()

    def _toggle_autostart(self):
        enabled = self.autostart_action.isChecked()
        self.settings.autostart = enabled
        self.settings.sync()
        autostart.set_enabled(enabled)

    def _on_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self._toggle_widget_visibility()

    def _quit(self):
        from PySide6.QtWidgets import QApplication
        QApplication.quit()

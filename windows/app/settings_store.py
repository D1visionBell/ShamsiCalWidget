"""Persisted user settings (position, theme, always-on-top, autostart)."""
from __future__ import annotations

from PySide6.QtCore import QSettings, QPoint

ORG = "D1visionBell"
APP = "ShamsiCalWidget"


class Settings:
    def __init__(self):
        self._qs = QSettings(QSettings.Format.IniFormat, QSettings.Scope.UserScope, ORG, APP)

    @property
    def dark_mode(self) -> bool:
        return self._qs.value("dark_mode", False, type=bool)

    @dark_mode.setter
    def dark_mode(self, value: bool):
        self._qs.setValue("dark_mode", value)

    @property
    def always_on_top(self) -> bool:
        return self._qs.value("always_on_top", True, type=bool)

    @always_on_top.setter
    def always_on_top(self, value: bool):
        self._qs.setValue("always_on_top", value)

    @property
    def autostart(self) -> bool:
        return self._qs.value("autostart", False, type=bool)

    @autostart.setter
    def autostart(self, value: bool):
        self._qs.setValue("autostart", value)

    @property
    def widget_pos(self) -> QPoint | None:
        pos = self._qs.value("widget_pos", None)
        return pos if isinstance(pos, QPoint) else None

    @widget_pos.setter
    def widget_pos(self, value: QPoint):
        self._qs.setValue("widget_pos", value)

    def sync(self):
        self._qs.sync()

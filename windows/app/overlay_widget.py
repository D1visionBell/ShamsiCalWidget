"""Frameless, always-on-top-toggleable floating widget that mirrors the
Android 2x2 home widget: weekday on top, big day number centered, month
+ year at the bottom, rounded card background."""
from __future__ import annotations

from PySide6.QtCore import Qt, QPoint, QRectF, Signal
from PySide6.QtGui import QPainter, QPainterPath, QColor, QMouseEvent
from PySide6.QtWidgets import QWidget, QMenu

import jalali
from settings_store import Settings
from resources_util import vazir_font

WIDGET_SIZE = 190
CORNER_RADIUS = 22

LIGHT_BG = QColor(255, 255, 255, 235)
LIGHT_PRIMARY = QColor(0, 0, 0)
LIGHT_SECONDARY = QColor(68, 68, 68)

DARK_BG = QColor(30, 30, 30, 235)
DARK_PRIMARY = QColor(255, 255, 255)
DARK_SECONDARY = QColor(204, 204, 204)


class OverlayWidget(QWidget):
    open_calendar_requested = Signal()
    exit_requested = Signal()

    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings
        self._drag_offset: QPoint | None = None
        self._dragged = False

        self.setFixedSize(WIDGET_SIZE, WIDGET_SIZE)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Tool
            | (Qt.WindowType.WindowStaysOnTopHint if settings.always_on_top else Qt.WindowType(0))
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)

        pos = settings.widget_pos
        if pos is not None:
            self.move(pos)

    # ---- painting -------------------------------------------------
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        date = jalali.today()  # always read live, never cached — avoids stale-date bugs

        dark = self.settings.dark_mode
        bg = DARK_BG if dark else LIGHT_BG
        primary = DARK_PRIMARY if dark else LIGHT_PRIMARY
        secondary = DARK_SECONDARY if dark else LIGHT_SECONDARY

        path = QPainterPath()
        path.addRoundedRect(QRectF(0, 0, WIDGET_SIZE, WIDGET_SIZE), CORNER_RADIUS, CORNER_RADIUS)
        painter.fillPath(path, bg)

        painter.setPen(primary)
        font_medium = vazir_font("Medium", 13)
        font_bold = vazir_font("Bold", 52)

        top_rect = QRectF(0, 14, WIDGET_SIZE, 26)
        painter.setFont(font_medium)
        painter.drawText(top_rect, Qt.AlignmentFlag.AlignCenter, date.day_name)

        center_rect = QRectF(0, 0, WIDGET_SIZE, WIDGET_SIZE)
        painter.setFont(font_bold)
        painter.drawText(center_rect, Qt.AlignmentFlag.AlignCenter, jalali.to_persian_digits(date.day))

        bottom_rect = QRectF(0, WIDGET_SIZE - 38, WIDGET_SIZE, 26)
        painter.setPen(secondary)
        painter.setFont(font_medium)
        month_year = f"{date.month_name} {jalali.to_persian_digits(date.year)}"
        painter.drawText(bottom_rect, Qt.AlignmentFlag.AlignCenter, month_year)

    # ---- live updates -----------------------------------------------
    def refresh_date(self):
        # No caching/comparison here on purpose: just force a repaint, and
        # paintEvent always reads the live date. Nothing to get stale.
        self.update()

    def apply_theme_change(self):
        self.update()

    def apply_on_top_change(self):
        was_visible = self.isVisible()
        flags = (
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Tool
            | (Qt.WindowType.WindowStaysOnTopHint if self.settings.always_on_top else Qt.WindowType(0))
        )
        self.setWindowFlags(flags)
        if was_visible:
            self.show()

    # ---- interaction ------------------------------------------------
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_offset = event.globalPosition().toPoint() - self.pos()
            self._dragged = False

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._drag_offset is not None:
            new_pos = event.globalPosition().toPoint() - self._drag_offset
            if (new_pos - self.pos()).manhattanLength() > 2:
                self._dragged = True
            self.move(new_pos)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            was_drag = self._dragged
            self._drag_offset = None
            self._dragged = False
            if not was_drag:
                self.open_calendar_requested.emit()
            else:
                self.settings.widget_pos = self.pos()
                self.settings.sync()

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        open_action = menu.addAction("باز کردن تقویم")
        menu.addSeparator()

        on_top_action = menu.addAction("همیشه روی صفحه")
        on_top_action.setCheckable(True)
        on_top_action.setChecked(self.settings.always_on_top)

        dark_action = menu.addAction("حالت تیره")
        dark_action.setCheckable(True)
        dark_action.setChecked(self.settings.dark_mode)

        menu.addSeparator()
        exit_action = menu.addAction("خروج")

        chosen = menu.exec(event.globalPos())
        if chosen == open_action:
            self.open_calendar_requested.emit()
        elif chosen == on_top_action:
            self.settings.always_on_top = not self.settings.always_on_top
            self.settings.sync()
            self.apply_on_top_change()
        elif chosen == dark_action:
            self.settings.dark_mode = not self.settings.dark_mode
            self.settings.sync()
            self.apply_theme_change()
        elif chosen == exit_action:
            self.exit_requested.emit()

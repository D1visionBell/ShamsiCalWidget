"""Full month-view calendar window, opened by clicking the overlay widget.

There is no equivalent "full app" screen in the original Android project
(it's a widget-only app with no launcher activity), so this view is new —
kept simple: a month grid with prev/next navigation and today highlighted.
"""
from __future__ import annotations

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton, QFrame
)

import jalali
from settings_store import Settings
from resources_util import vazir_font

WEEKDAY_HEADERS = ["ی", "د", "س", "چ", "پ", "ج", "ش"]  # Sunday..Saturday, matches DAY_NAMES order


class CalendarWindow(QWidget):
    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings
        self.setWindowTitle("تقویم شمسی")
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.resize(360, 400)

        today = jalali.today()
        self._view_year = today.year
        self._view_month = today.month

        self._root = QVBoxLayout(self)

        header = QHBoxLayout()
        self._prev_btn = QPushButton("قبلی")
        self._next_btn = QPushButton("بعدی")
        self._title_label = QLabel()
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._title_label.setFont(vazir_font("Bold", 14))
        self._prev_btn.clicked.connect(self._go_prev)
        self._next_btn.clicked.connect(self._go_next)
        header.addWidget(self._next_btn)
        header.addWidget(self._title_label, stretch=1)
        header.addWidget(self._prev_btn)
        self._root.addLayout(header)

        self._grid_container = QWidget()
        self._root.addWidget(self._grid_container)

        self._render_month()

        # Keep the "today" highlight correct if this window is left open
        # across a date change (e.g. midnight).
        self._refresh_timer = QTimer(self)
        self._refresh_timer.timeout.connect(self._render_month)
        self._refresh_timer.start(20_000)

    def _go_prev(self):
        self._view_year, self._view_month = jalali.add_months(self._view_year, self._view_month, -1)
        self._render_month()

    def _go_next(self):
        self._view_year, self._view_month = jalali.add_months(self._view_year, self._view_month, 1)
        self._render_month()

    def _render_month(self):
        first_day = jalali.from_ymd(self._view_year, self._view_month, 1)
        days_in_month = first_day.days_in_month()
        today = jalali.today()

        self._title_label.setText(
            f"{first_day.month_name} {jalali.to_persian_digits(self._view_year)}"
        )

        old_layout = self._grid_container.layout()
        if old_layout is not None:
            while old_layout.count():
                item = old_layout.takeAt(0)
                w = item.widget()
                if w:
                    w.deleteLater()
            QWidget().setLayout(old_layout)  # detach

        grid = QGridLayout(self._grid_container)
        grid.setSpacing(4)

        for col, header_text in enumerate(WEEKDAY_HEADERS):
            lbl = QLabel(header_text)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lbl.setFont(vazir_font("Medium", 10))
            grid.addWidget(lbl, 0, col)

        row = 1
        col = first_day.weekday_index  # 0=Sunday .. matches column order above
        for day in range(1, days_in_month + 1):
            cell = QLabel(jalali.to_persian_digits(day))
            cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cell.setFixedHeight(36)
            cell.setFont(vazir_font("Medium", 12))
            is_today = (
                today.year == self._view_year
                and today.month == self._view_month
                and today.day == day
            )
            if is_today:
                cell.setStyleSheet(
                    "background-color: #2f6fed; color: white; border-radius: 6px;"
                )
            grid.addWidget(cell, row, col)
            col += 1
            if col > 6:
                col = 0
                row += 1

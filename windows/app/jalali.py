"""
Jalali calendar helpers.

Ported logic/strings from the Android project's JalaliCalendar.kt so the
displayed day/month names and Persian-digit formatting are identical to the
Android widget. The actual Gregorian<->Jalali math is delegated to the
well-tested `jdatetime` library instead of re-porting the hand-rolled Kotlin
algorithm — same result, fewer places for an edge-case bug to hide.
"""
from __future__ import annotations

from dataclasses import dataclass
import jdatetime

MONTH_NAMES = [
    "فروردین", "اردیبهشت", "خرداد",
    "تیر", "مرداد", "شهریور",
    "مهر", "آبان", "آذر",
    "دی", "بهمن", "اسفند",
]

# Index 0 = Sunday .. 6 = Saturday (matches Kotlin's dayNames[1..7] shifted by one)
DAY_NAMES = ["یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه", "شنبه"]

_PERSIAN_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

_MONTH_DAYS = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]


def to_persian_digits(value: int) -> str:
    return str(value).translate(_PERSIAN_DIGITS)


@dataclass(frozen=True)
class JalaliDate:
    year: int
    month: int
    day: int
    weekday_index: int  # 0=Sunday .. 6=Saturday

    @property
    def day_name(self) -> str:
        return DAY_NAMES[self.weekday_index]

    @property
    def month_name(self) -> str:
        return MONTH_NAMES[self.month - 1]

    def is_leap_year(self) -> bool:
        return jdatetime.date(self.year, 1, 1).isleap()

    def days_in_month(self) -> int:
        if self.month == 12:
            return 30 if self.is_leap_year() else 29
        return _MONTH_DAYS[self.month - 1]


def _weekday_index(g_weekday: int) -> int:
    # Python's date.weekday(): Monday=0 .. Sunday=6
    # We want: Sunday=0 .. Saturday=6
    return (g_weekday + 1) % 7


def today() -> JalaliDate:
    jd = jdatetime.date.today()
    g_weekday = jd.togregorian().weekday()
    return JalaliDate(jd.year, jd.month, jd.day, _weekday_index(g_weekday))


def from_ymd(year: int, month: int, day: int) -> JalaliDate:
    jd = jdatetime.date(year, month, day)
    g_weekday = jd.togregorian().weekday()
    return JalaliDate(year, month, day, _weekday_index(g_weekday))


def add_months(year: int, month: int, delta: int) -> tuple[int, int]:
    """Return (year, month) shifted by delta months (can be negative)."""
    index0 = (month - 1) + delta
    year += index0 // 12
    month = index0 % 12 + 1
    return year, month

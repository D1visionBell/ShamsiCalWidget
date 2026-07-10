# ShamsiCalWidget — نسخه‌ی ویندوز (PySide6)


این پوشه یک ساب‌پروژه‌ی مستقل پایتونی/PySide6 هست، کنار پروژه‌ی اصلی اندروید (Kotlin/Gradle) تو همین ریپو.

## ساختار
```
windows/
  build.spec              فایل PyInstaller
  build.bat               اسکریپت خودکار ساخت exe
  requirements.txt
  app/
    main.py                نقطه‌ی ورود
    jalali.py              منطق تاریخ جلالی (بر پایه‌ی jdatetime)
    overlay_widget.py       ویجت شناور ۲×۲ (قابل درگ، راست‌کلیک = منو)
    calendar_window.py      پنجره‌ی تقویم کامل ماهانه (با کلیک روی ویجت باز می‌شه)
    tray.py                 آیکون سیستم‌تری
    settings_store.py       ذخیره‌ی موقعیت/تم/always-on-top (QSettings)
    autostart.py            اجرا با ویندوز (رجیستری HKCU Run)
    resources_util.py       پیدا کردن مسیر فونت/آیکون چه در dev چه در exe
    resources/
      fonts/vazirmatn_medium.ttf, vazirmatn_bold.ttf
      icon.ico
```


## اجرا برای تست (بدون build)
```
pip install -r requirements.txt
python app/main.py
```

## ساخت exe
روی ویندوز (PyInstaller نمی‌تونه از لینوکس/مک برای ویندوز کراس‌کامپایل کنه،
باید خود ویندوز باشه):
```
build.bat
```
یا دستی:
```
pip install -r requirements.txt pyinstaller
pyinstaller build.spec
```
خروجی: `dist\ShamsiCalWidget.exe` — تک‌فایلی، بدون کنسول.
.

## رفتار
- **باز شدن**: پنجره‌ی کوچیک شناور گوشه‌ای از صفحه (موقعیت پیش‌فرض رو با
  درگ کردن جابه‌جا کن، خودش ذخیره می‌شه).
- **کلیک ساده روی ویجت** → باز شدن تقویم کامل ماهانه.
- **درگ کردن** → جابه‌جایی ویجت (کلیک محسوب نمی‌شه، تقویم باز نمی‌شه).
- **راست‌کلیک روی ویجت یا آیکون تری** → منو: باز کردن تقویم، توگل
  "همیشه روی صفحه" (خروج/ورود به حالت ontop)، توگل حالت تیره، اجرا با
  ویندوز، خروج.
- **کلیک چپ روی آیکون تری** → نمایش/مخفی کردن ویجت.
- تاریخ هر ۶۰ ثانیه چک می‌شه.
.

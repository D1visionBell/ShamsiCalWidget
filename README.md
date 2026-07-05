<div align="center">

<img src="app/src/main/res/mipmap-xxxhdpi/ic_launcher.png" width="144">

# ShamsiCal Widget

### ویجت تقویم شمسی برای اندروید

تقویم شمسی مینیمال برای صفحه اصلی و صفحه قفل اندروید

الهام گرفته از اپ **ShamsiCal** برای iOS

<p align="center">
<img src="https://img.shields.io/badge/Android-8%2B-3DDC84">
<img src="https://img.shields.io/badge/Widgets-3-blue">
<img src="https://img.shields.io/badge/Theme-Light%20%26%20Dark-6f42c1">
<img src="https://img.shields.io/badge/Language-FA-orange">
</p>

</div>

---

## ✨ ویجت‌ها

### 🗓 ویجت 2×2 صفحه اصلی

نمایش روز هفته، عدد روز و ماه شمسی در قالبی مینیمال و خوانا.

### 📝 ویجت متنی 3×1

نمایش فشرده تاریخ شمسی برای کاربرانی که طراحی ساده‌تر را ترجیح می‌دهند.

<div align="right">

• هماهنگ با طراحی ویجت اصلی<br>
• پس‌زمینه روشن در Light Mode<br>
• پس‌زمینه تیره در Dark Mode

</div>

<p align="center">
<img src="assets/HomeScreen.jpg" width="260">
</p>

---

### 🔒 ویجت صفحه قفل

نمایش افقی روز، عدد و ماه شمسی روی صفحه قفل.

<div align="right">

پشتیبانی از:

• Samsung One UI<br>
• Good Lock<br>
• LockStar<br>
• برخی لانچرهای شخص ثالث

</div>

<p align="center">
<img src="assets/LockScreen.jpg" width="260">
</p>

---

## 🚀 امکانات

<div align="right">

✅ تقویم شمسی دقیق و مستقل<br>
✅ پشتیبانی از صفحه اصلی و صفحه قفل<br>
✅ طراحی مینیمال<br>
✅ سازگار با Dark Mode<br>
✅ بروزرسانی خودکار در ابتدای هر روز<br>
✅ بازیابی خودکار پس از راه‌اندازی مجدد دستگاه<br>
✅ فونت Vazirmatn<br>
✅ گوشه‌های گرد و طراحی مدرن<br>
✅ مصرف بسیار کم باتری

</div>

---

## 🏗 معماری پروژه

```text
app/src/main/
├── AndroidManifest.xml
├── java/com/shamsicalwidget/
│
├── util/
│   └── JalaliCalendar.kt
│
├── widget/
│   ├── HomeWidgetProvider.kt
│   ├── HomeTextWidgetProvider.kt
│   ├── LockScreenWidgetProvider.kt
│   ├── WidgetUpdateService.kt
│   └── BootReceiver.kt
│
└── res/
    ├── drawable/
    │   └── widget_background.xml
    │
    ├── font/
    │   ├── vazirmatn_medium.ttf
    │   ├── vazirmatn_bold.ttf
    │   └── fonts.xml
    │
    ├── layout/
    │   ├── widget_home.xml
    │   ├── widget_home_text.xml
    │   └── widget_lock.xml
    │
    ├── values/
    │   ├── colors.xml
    │   ├── strings.xml
    │   └── themes.xml
    │
    ├── values-night/
    │   └── colors.xml
    │
    └── xml/
        ├── home_widget_info.xml
        ├── home_text_widget_info.xml
        └── lock_widget_info.xml
```

---

## 📲 نصب ویجت

### صفحه اصلی

1. صفحه اصلی را لمس و نگه دارید.
2. وارد بخش **Widgets** شوید.
3. **ShamsiCal Widget** را انتخاب کنید.
4. یکی از ویجت‌های زیر را اضافه کنید.

<div align="right">

🗓 تقویم شمسی 2×2<br>
📝 تقویم شمسی متنی 3×1

</div>

---

### صفحه قفل

برای دستگاه‌های سازگار:

1. صفحه قفل را لمس و نگه دارید.
2. وارد بخش **Widgets** شوید.
3. ویجت **تقویم شمسی (Lock Screen)** را انتخاب کنید.

---

## ⚠️ سازگاری

<table align="center">

<tr>
<th>دستگاه</th>
<th>پشتیبانی</th>
</tr>

<tr>
<td>Samsung One UI 5+</td>
<td align="center">✅</td>
</tr>

<tr>
<td>Samsung One UI 6+</td>
<td align="center">✅</td>
</tr>

<tr>
<td>Good Lock + LockStar</td>
<td align="center">✅</td>
</tr>

<tr>
<td>Pixel Launcher</td>
<td align="center">❌</td>
</tr>

<tr>
<td>AOSP</td>
<td align="center">❌</td>
</tr>

<tr>
<td>لانچرهای شخص ثالث</td>
<td align="center">⚠️ محدود</td>
</tr>

</table>

---

## 🎨 طراحی

<div align="right">

• فونت: **Vazirmatn**<br>
• گوشه‌های گرد<br>
• Light & Dark Theme<br>
• طراحی مینیمال و خوانا<br>
• هماهنگ با زبان فارسی

</div>

---

<div align="center">

ساخته شده برای کاربرانی که یک تقویم شمسی ساده، زیبا و همیشه در دسترس می‌خواهند.

</div>

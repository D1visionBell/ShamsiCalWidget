<div align="center">

<img src="app/src/main/res/mipmap-xxxhdpi/ic_launcher.webp" width="144">

# ShamsiCal Widget

### ویجت تقویم شمسی برای اندروید

تقویم شمسی مینیمال برای صفحه اصلی و صفحه قفل اندروید
الهام گرفته از اپ **ShamsiCal** برای iOS

<br>

<img src="assets/home_widget.png" width="250">
<img src="assets/home_text_widget.png" width="250">
<img src="assets/lock_widget.png" width="250">

</div>

---

## ✨ ویجت‌ها

### 🗓 ویجت 2×2 صفحه اصلی

نمایش روز هفته، عدد روز و ماه شمسی در قالبی مینیمال و خوانا.

```
┌─────────────────────┐
│       پنجشنبه       │
│                     │
│          ۴          │
│                     │
│      تیر ۱۴۰۵       │
└─────────────────────┘
```

---

### 📝 ویجت متنی 3×1

نمایش فشرده تاریخ شمسی برای کاربرانی که طراحی ساده‌تر را ترجیح می‌دهند.

```
┌──────────────────────────────┐
│        پنجشنبه ۴ تیر         │
└──────────────────────────────┘
```

* هماهنگ با طراحی ویجت اصلی
* پس‌زمینه روشن در Light Mode
* پس‌زمینه تیره در Dark Mode

---

### 🔒 ویجت صفحه قفل

نمایش افقی روز، عدد و ماه شمسی روی صفحه قفل.

پشتیبانی از:

* Samsung One UI
* Good Lock
* LockStar
* برخی لانچرهای شخص ثالث

از طریق:

```xml
widgetCategory="keyguard|home_screen"
```

---

## 🚀 امکانات

* ✅ تقویم شمسی دقیق و مستقل
* ✅ پشتیبانی از صفحه اصلی و صفحه قفل
* ✅ طراحی مینیمال
* ✅ سازگار با Dark Mode
* ✅ بروزرسانی خودکار در ابتدای هر روز
* ✅ بازیابی خودکار پس از راه‌اندازی مجدد دستگاه
* ✅ فونت زیبای Vazirmatn
* ✅ گوشه‌های گرد و طراحی مدرن
* ✅ مصرف بسیار کم باتری

---

## 📸 پیش‌نمایش

<div align="center">

<img src="assets/home_widget.png" width="240">

<img src="assets/home_text_widget.png" width="240">

<img src="assets/lock_widget.png" width="240">

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
4. یکی از ویجت‌های زیر را اضافه کنید:

* 🗓 تقویم شمسی 2×2
* 📝 تقویم شمسی متنی 3×1

---

### صفحه قفل

برای دستگاه‌های سازگار:

1. صفحه قفل را لمس و نگه دارید.
2. وارد بخش **Widgets** شوید.
3. ویجت **تقویم شمسی (Lock Screen)** را انتخاب کنید.

---

## ⚠️ سازگاری

| دستگاه               | پشتیبانی |
| -------------------- | -------- |
| Samsung One UI 5+    | ✅        |
| Samsung One UI 6+    | ✅        |
| Good Lock + LockStar | ✅        |
| Pixel Launcher       | ❌        |
| AOSP                 | ❌        |
| لانچرهای شخص ثالث    | ⚠️ محدود |

---

## 🎨 طراحی

* فونت: **Vazirmatn**
* گوشه‌های گرد
* Light & Dark Theme
* طراحی مینیمال و خوانا
* هماهنگ با زبان فارسی

---

<div align="center">

ساخته شده برای کاربرانی که یک تقویم شمسی ساده، زیبا و همیشه در دسترس می‌خواهند.

</div>

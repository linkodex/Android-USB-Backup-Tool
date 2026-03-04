# Android USB Backup Tool 📱💾

[Azərbaycan dili](#azərbaycan-dili) | [English](#english)

---

## Azərbaycan Dili

Bu skript Android cihazındakı daxili yaddaşı (/sdcard) avtomatik analiz edir və faylları kateqoriyalar üzrə xarici USB fləş karta kopyalayır.

### ✨ Özəlliklər
- **Ağıllı Çeşidləmə:** Faylları uzantılarına görə (Fotolar, Videolar və s.) qovluqlara ayırır.
- **Təhlükəsizlik:** USB tapılmadıqda daxili yaddaşın dolmaması üçün prosesi dayandırır.
- **Dublikat Qoruması:** Eyni adlı faylların üzərinə yazmır, nömrələyərək saxlayır.

### 🚀 Quraşdırma
```bash
chmod +x setup.sh
./setup.sh
python smart_copy.py
```

---

## English

This script automatically analyzes the internal storage (/sdcard) of an Android device and copies files to an external USB flash drive, categorized by type.

### ✨ Features
- **Smart Sorting:** Organizes files into folders based on extensions (Photos, Videos, etc.).
- **Safety First:** Aborts the process if no USB is detected to prevent filling up internal storage.
- **Duplicate Protection:** Does not overwrite existing files; instead, it renames them with a counter.

### 🚀 Installation
```bash
chmod +x setup.sh
./setup.sh
python smart_copy.py
```

## 🛠️ Requirements
- Python 3.x
- `tqdm` library (`pip install tqdm`)

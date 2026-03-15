# Android USB Backup Tool 📱💾

[Azərbaycan dili](#azərbaycan-dili) | [English](#english)

---

## Azərbaycan Dili

Bu skript Android cihazındakı daxili yaddaşı (/sdcard) avtomatik analiz edir və faylları kateqoriyalar üzrə xarici USB fləş karta kopyalayır.

### ✨ Özəlliklər
- **Ağıllı Çeşidləmə:** Faylları uzantılarına görə (Fotolar, Videolar və s.) qovluqlara ayırır.
- **Təhlükəsizlik:** USB tapılmadıqda daxili yaddaşın dolmaması üçün prosesi dayandırır.
- **Yaddaş Yoxlaması:** Backup başlamazdan əvvəl USB-də kifayət qədər boş yer olub-olmadığını yoxlayır.
- **Dublikat Qoruması:** Eyni adlı faylların üzərinə yazmır, nömrələyərək saxlayır.
- **Xəta Loqu:** Kopyalana bilməyən fayllar `backup_errors.log` faylına yazılır.

---

### 📋 Tələblər
- Android cihaz + [Termux](https://termux.dev) tətbiqi
- OTG dəstəkli USB fləş kart
- Python 3.x
- `tqdm` kitabxanası (setup.sh tərəfindən avtomatik quraşdırılır)

---

### 🚀 Quraşdırma və İstifadə

**Addım 1 — Termux-u yükləyin**

[F-Droid](https://f-droid.org) və ya [termux.dev](https://termux.dev) saytından Termux tətbiqini yükləyin və quraşdırın.
> ⚠️ Google Play-dəki köhnəlmiş versiyadan istifadə etməyin.

---

**Addım 2 — Faylları cihaza köçürün**

Kompüterdən `smart_copy.py` və `setup.sh` fayllarını telefona köçürün (USB, Bluetooth və ya birbaşa yükləmə ilə).

---

**Addım 3 — Termux-da qovluğa keçin**

```bash
cd /sdcard/Download
```
> Faylları harda saxladınızsa həmin qovluğa keçin.

---

**Addım 4 — setup.sh faylına icazə verin**

```bash
chmod +x setup.sh
```

---

**Addım 5 — Setup skriptini işə salın**

```bash
./setup.sh
```

Bu addımda setup.sh avtomatik olaraq aşağıdakıları edir:
- Sistem paketlərini yeniləyir
- Python quraşdırılıbsa yoxlayır, yoxdursa quraşdırır
- `tqdm` kitabxanasını quraşdırır
- Yaddaş icazəsi istəyir — **ekranda çıxan pəncərədə "İcazə Ver" (Allow) seçin!**
- `smart_copy.py` faylının mövcudluğunu yoxlayır

---

**Addım 6 — USB fləşi qoşun**

OTG adapter vasitəsilə USB fləş kartı telefona qoşun.

---

**Addım 7 — Backup skriptini işə salın**

```bash
python smart_copy.py
```

---

### 📁 Yaradılan Qovluq Strukturu

USB fləşdə `PhoneCopy/` qovluğu altında aşağıdakı kateqoriyalar yaradılır:

| Qovluq | Fayl növləri |
|---|---|
| `Fotolar` | .jpg, .jpeg, .png, .webp, .heic, .gif |
| `Videolar` | .mp4, .mkv, .mov, .avi, .3gp |
| `Fayllar` | .pdf, .docx, .txt, .zip, .rar, .apk, .xlsx |
| `HiddenFiles` | Gizli fayllar (nöqtə ilə başlayanlar) |
| `Temp` | .tmp, .temp, .log |
| `cache` | Cache qovluqlarındakı fayllar |
| `Thumbnails` | Miniatür şəkillər |

---

### ⚠️ Qeydlər
- Backup zamanı xəta baş verərsə, detallar `backup_errors.log` faylında saxlanılır.
- USB-də yetərli boş yer olmadıqda skript backup başlamazdan əvvəl xəbərdarlıq verib dayanır.

---

## English

This script automatically analyzes the internal storage (/sdcard) of an Android device and copies files to an external USB flash drive, categorized by type.

### ✨ Features
- **Smart Sorting:** Organizes files into folders based on extensions (Photos, Videos, etc.).
- **Safety First:** Aborts the process if no USB is detected to prevent filling up internal storage.
- **Storage Check:** Verifies that the USB drive has enough free space before starting the backup.
- **Duplicate Protection:** Does not overwrite existing files; instead, it renames them with a counter.
- **Error Logging:** Files that cannot be copied are recorded in `backup_errors.log`.

---

### 📋 Requirements
- Android device + [Termux](https://termux.dev) app
- OTG-compatible USB flash drive
- Python 3.x
- `tqdm` library (installed automatically by setup.sh)

---

### 🚀 Installation & Usage

**Step 1 — Install Termux**

Download and install Termux from [F-Droid](https://f-droid.org) or [termux.dev](https://termux.dev).
> ⚠️ Do not use the outdated version from Google Play.

---

**Step 2 — Transfer files to your device**

Copy `smart_copy.py` and `setup.sh` to your phone via USB, Bluetooth, or direct download.

---

**Step 3 — Navigate to the folder in Termux**

```bash
cd /sdcard/Download
```
> Navigate to wherever you saved the files.

---

**Step 4 — Give execute permission to setup.sh**

```bash
chmod +x setup.sh
```

---

**Step 5 — Run the setup script**

```bash
./setup.sh
```

This step automatically:
- Updates system packages
- Checks if Python is installed, installs it if not
- Installs the `tqdm` library
- Requests storage permission — **tap "Allow" on the popup that appears!**
- Verifies that `smart_copy.py` exists

---

**Step 6 — Connect your USB drive**

Plug in your USB flash drive via an OTG adapter.

---

**Step 7 — Run the backup script**

```bash
python smart_copy.py
```

---

### 📁 Folder Structure

The following categories are created under the `PhoneCopy/` folder on your USB drive:

| Folder | File types |
|---|---|
| `Fotolar` | .jpg, .jpeg, .png, .webp, .heic, .gif |
| `Videolar` | .mp4, .mkv, .mov, .avi, .3gp |
| `Fayllar` | .pdf, .docx, .txt, .zip, .rar, .apk, .xlsx |
| `HiddenFiles` | Hidden files (starting with a dot) |
| `Temp` | .tmp, .temp, .log |
| `cache` | Files from cache directories |
| `Thumbnails` | Thumbnail images |

---

### ⚠️ Notes
- If any errors occur during backup, details are saved in `backup_errors.log`.
- If the USB drive does not have enough free space, the script will warn you and stop before starting the backup.

---

## 🛠️ Requirements Summary
- Python 3.x
- `tqdm` library (`pip install tqdm`)

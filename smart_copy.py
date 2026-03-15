import os
import shutil
import subprocess
import sys
from tqdm import tqdm

# --- DİNAMİK YOLLARIN TƏYİNİ ---
internal_storage = "/sdcard"
ERROR_LOG = "backup_errors.log"

def get_usb_path():
    """Qoşulmuş USB fləş kartın yolunu tapır"""
    storage_base = "/storage"
    try:
        for entry in os.listdir(storage_base):
            # /storage/XXXX-XXXX formatında xarici yaddaş axtarırıq
            if "-" in entry and entry not in ("self", "emulated"):
                full_path = os.path.join(storage_base, entry)
                if os.path.isdir(full_path):
                    return full_path
    except Exception:
        return None
    return None

def check_usb_space(usb_path, source_path):
    """USB-də kifayət qədər boş yer olub-olmadığını yoxlayır"""
    try:
        source_usage = shutil.disk_usage(source_path)
        usb_free = shutil.disk_usage(usb_path).free
        needed_mb = source_usage.used // 1024 // 1024
        free_mb = usb_free // 1024 // 1024
        if usb_free < source_usage.used:
            print("\n" + "="*40)
            print("❌ SƏHV: USB-də kifayət qədər yer yoxdur!")
            print(f"   Lazım olan: {needed_mb} MB")
            print(f"   Mövcud:     {free_mb} MB")
            print("="*40 + "\n")
            sys.exit(1)
        else:
            print(f"✅ USB yaddaşı kifayətdir. Mövcud: {free_mb} MB")
    except Exception as e:
        print(f"⚠️  Yaddaş yoxlanışı zamanı xəta: {e}")

# USB-ni yoxlayırıq
usb_path = get_usb_path()

if not usb_path:
    print("\n" + "="*40)
    print("❌ SƏHV: USB fləş kart tapılmadı!")
    print("👉 Zəhmət olmasa OTG qoşun və ya USB-ni aktiv edin.")
    print("⚠️  Daxili yaddaşın dolmaması üçün proses dayandırıldı.")
    print("="*40 + "\n")
    sys.exit(1)

# USB yaddaşını yoxlayırıq
check_usb_space(usb_path, internal_storage)

# Əgər bura çatdıqsa, deməli USB tapılıb və yer kifayətdir
dest_root = os.path.join(usb_path, "PhoneCopy")

# Qovluq strukturu və uzantılar
# Qeyd: "HiddenFiles", "cache", "Thumbnails" kateqoriyaları
# fayl yoluna görə get_category() içində müəyyən edilir,
# uzantı siyahısı ilə deyil.
folders = {
    "Fotolar":     [".jpg", ".jpeg", ".png", ".webp", ".heic", ".gif"],
    "Videolar":    [".mp4", ".mkv", ".mov", ".avi", ".3gp"],
    "Fayllar":     [".pdf", ".docx", ".txt", ".zip", ".rar", ".apk", ".xlsx"],
    "HiddenFiles": [],
    "Temp":        [".tmp", ".temp", ".log"],
    "cache":       [],
    "Thumbnails":  [],
}

stats = {k: 0 for k in folders.keys()}
error_count = 0

def create_dirs():
    """USB daxilində qovluqları yaradır"""
    os.makedirs(dest_root, exist_ok=True)
    for folder in folders.keys():
        os.makedirs(os.path.join(dest_root, folder), exist_ok=True)

def get_category(filename, filepath):
    lower_path = filepath.lower()
    lower_file = filename.lower()

    if "thumb" in lower_path or ".thumbnails" in lower_path:
        return "Thumbnails"
    if "cache" in lower_path:
        return "cache"
    if lower_file.startswith('.') or '/.' in filepath:
        return "HiddenFiles"
    if "temp" in lower_path or "tmp" in lower_path:
        return "Temp"

    ext = os.path.splitext(lower_file)[1]
    for cat, exts in folders.items():
        if ext in exts:
            return cat
    return "Fayllar"

def start_copy():
    global error_count
    all_files = []
    print(f"📂 Mənbə: {internal_storage}")
    print(f"💾 Hədəf (USB): {dest_root}")
    print("🔍 Analiz edilir... (Bu bir az vaxt ala bilər)")

    for root, dirs, files in os.walk(internal_storage):
        for file in files:
            all_files.append(os.path.join(root, file))

    total = len(all_files)
    if total == 0:
        print("⚠️ Heç bir fayl tapılmadı. İcazələri yoxlayın!")
        return

    print(f"📦 Cəmi {total} fayl aşkarlandı.")

    with tqdm(total=total, desc="Gedişat", unit="fayl") as pbar:
        for file_path in all_files:
            try:
                file_name = os.path.basename(file_path)
                category = get_category(file_name, file_path)

                target_dir = os.path.join(dest_root, category)
                target_file = os.path.join(target_dir, file_name)

                counter = 1
                base, extension = os.path.splitext(file_name)
                while os.path.exists(target_file):
                    target_file = os.path.join(target_dir, f"{base}_{counter}{extension}")
                    counter += 1

                shutil.copy2(file_path, target_file)
                stats[category] += 1

            except Exception as e:
                error_count += 1
                try:
                    with open(ERROR_LOG, "a", encoding="utf-8") as log:
                        log.write(f"SƏHV: {file_path} → {e}\n")
                except Exception:
                    pass
            finally:
                pbar.update(1)

    print("\n" + "="*35)
    print("✅ BACKUP TAMAMLANDI (USB-YƏ)")
    print("="*35)
    for cat, count in stats.items():
        if count > 0:
            print(f"🔹 {cat.ljust(12)}: {count} fayl")
    print("="*35)

    if error_count > 0:
        print(f"⚠️  {error_count} fayl kopyalana bilmədi. Təfərrüat: {ERROR_LOG}")
    else:
        print("🎉 Bütün fayllar uğurla kopyalandı!")

if __name__ == "__main__":
    create_dirs()
    start_copy()

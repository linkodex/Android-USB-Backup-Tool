import os
import shutil
import subprocess
import sys
from tqdm import tqdm

# --- DİNAMİK YOLLARIN TƏYİNİ ---
internal_storage = "/sdcard" 

def get_usb_path():
    """Qoşulmuş USB fləş kartın yolunu tapır"""
    try:
        output = subprocess.check_output("df", shell=True).decode()
        for line in output.split('\n'):
            # Android-də xarici yaddaş adətən /storage/XXXX-XXXX şəklində olur
            if "/storage/" in line and "-" in line:
                return line.split()[-1]
    except:
        return None
    return None

# USB-ni yoxlayırıq
usb_path = get_usb_path()

if not usb_path:
    print("\n" + "="*40)
    print("❌ SƏHV: USB fləş kart tapılmadı!")
    print("👉 Zəhmət olmasa OTG qoşun və ya USB-ni aktiv edin.")
    print("⚠️  Daxili yaddaşın dolmaması üçün proses dayandırıldı.")
    print("="*40 + "\n")
    sys.exit() # Skripti tamamilə dayandırır

# Əgər bura çatdıqsa, deməli USB tapılıb
dest_root = os.path.join(usb_path, "PhoneCopy")

# Qovluq strukturu və uzantılar
folders = {
    "Fotolar": [".jpg", ".jpeg", ".png", ".webp", ".heic", ".gif"],
    "Videolar": [".mp4", ".mkv", ".mov", ".avi", ".3gp"],
    "Fayllar": [".pdf", ".docx", ".txt", ".zip", ".rar", ".apk", ".xlsx"],
    "HiddenFiles": ["hidden"],
    "Temp": [".tmp", ".temp", ".log"],
    "cache": ["cache"],
    "Thumbnails": ["thumb", ".thumbnails"]
}

stats = {k: 0 for k in folders.keys()}

def create_dirs():
    """USB daxilində qovluqları yaradır"""
    if not os.path.exists(dest_root):
        os.makedirs(dest_root, exist_ok=True)
    for folder in folders.keys():
        os.makedirs(os.path.join(dest_root, folder), exist_ok=True)

def get_category(filename, filepath):
    lower_path = filepath.lower()
    lower_file = filename.lower()
    
    if "thumb" in lower_path or ".thumbnails" in lower_path: return "Thumbnails"
    if "cache" in lower_path: return "cache"
    if lower_file.startswith('.') or '/.' in filepath: return "HiddenFiles"
    if "temp" in lower_path or "tmp" in lower_path: return "Temp"

    ext = os.path.splitext(lower_file)[1]
    for cat, exts in folders.items():
        if ext in exts:
            return cat
    return "Fayllar"

def start_copy():
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
            except:
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

if __name__ == "__main__":
    create_dirs()
    start_copy()

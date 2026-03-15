#!/data/data/com.termux/files/usr/bin/bash

echo "------------------------------------------"
echo "🚀 ANDROID HAZIRLIQ VƏ QURAŞDIRMA SİSTEMİ"
echo "------------------------------------------"

# 1. Paketləri yeniləyirik
echo "🔄 [1/5] Sistem paketləri yenilənir..."
pkg update -y && pkg upgrade -y || {
    echo "❌ Paket yeniləməsi uğursuz oldu!"
    exit 1
}

# 2. Python-un olub-olmadığını yoxlayırıq
if ! command -v python &> /dev/null; then
    echo "🐍 [2/5] Python tapılmadı. Quraşdırılır..."
    pkg install python python-pip -y || {
        echo "❌ Python quraşdırıla bilmədi!"
        exit 1
    }
else
    echo "✅ [2/5] Python artıq quraşdırılıb."
fi

# 3. Lazımi kitabxananı (tqdm) quraşdırırıq
echo "📦 [3/5] Python kitabxanaları (tqdm) yüklənir..."
pip install tqdm || {
    echo "❌ tqdm quraşdırıla bilmədi!"
    exit 1
}

# 4. Yaddaş icazəsini istəyirik
echo "📂 [4/5] Yaddaş icazəsi yoxlanılır..."
if [ ! -d "$HOME/storage" ]; then
    echo "⚠️  EKRANDA ÇIXAN PƏNCƏRƏDƏ 'İCAZƏ VER' (ALLOW) SEÇİN!"
    termux-setup-storage
    sleep 5
else
    echo "✅ [4/5] Yaddaş icazəsi artıq var."
fi

# 5. smart_copy.py faylının mövcudluğunu yoxlayırıq
echo "🔎 [5/5] smart_copy.py faylı yoxlanılır..."
if [ ! -f "smart_copy.py" ]; then
    echo "❌ smart_copy.py tapılmadı!"
    echo "👉 Zəhmət olmasa düzgün qovluqda olduğunuzu yoxlayın."
    echo "   Məsələn: cd Android-USB-Backup-Tool && ./setup.sh"
    exit 1
else
    echo "✅ [5/5] smart_copy.py tapıldı."
fi

echo "------------------------------------------"
echo "🎉 HƏR ŞEY HAZIRDIR!"
echo "İndi 'python smart_copy.py' yazıb başlaya bilərsiniz."
echo "------------------------------------------"

# scriptə icazə vermək və işə salmaq qaydası:
# chmod +x setup.sh
# ./setup.sh

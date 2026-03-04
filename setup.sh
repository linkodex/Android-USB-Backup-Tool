#!/data/data/com.termux/files/usr/bin/bash

echo "------------------------------------------"
echo "🚀 ANDROID HAZIRLIQ VƏ QURAŞDIRMA SİSTEMİ"
echo "------------------------------------------"

# 1. Paketləri yeniləyirik
echo "🔄 [1/4] Sistem paketləri yenilənir..."
pkg update -y && pkg upgrade -y

# 2. Python-un olub-olmadığını yoxlayırıq
if ! command -v python &> /dev/null
then
    echo "🐍 [2/4] Python tapılmadı. Quraşdırılır..."
    pkg install python python-pip -y
else
    echo "✅ [2/4] Python artıq quraşdırılıb."
fi

# 3. Lazımi kitabxananı (tqdm) yazırıq
echo "📦 [3/4] Python kitabxanaları (tqdm) yüklənir..."
pip install tqdm

# 4. Yaddaş icazəsini istəyirik
echo "📂 [4/4] Yaddaş icazəsi yoxlanılır..."
if [ ! -d "$HOME/storage" ]; then
    echo "⚠️  EKRANDA ÇIXAN PƏNCƏRƏDƏ 'İCAZƏ VER' (ALLOW) SEÇİN!"
    termux-setup-storage
    sleep 5
else
    echo "✅ [4/4] Yaddaş icazəsi artıq var."
fi

echo "------------------------------------------"
echo "🎉 HƏR ŞEY HAZIRDIR!"
echo "İndi 'python smart_copy.py' yazıb başlaya bilərsiniz."
echo "------------------------------------------"

# scriptə icazə və işə salmaq qaydası
# chmod +x setup.sh
# ./setup.sh


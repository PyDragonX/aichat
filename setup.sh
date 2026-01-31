#!/bin/bash
# تنظيف الشاشة لإظهار شعار التنين
clear
echo "🐉 PyDragonX Installer is starting..."
sleep 2
# تحديث النظام وتثبيت المتطلبات
echo " [!] Updating system packages..."
apt update && apt upgrade -y
echo " [!] Installing Python..."
pkg install python -y
# تثبيت المكتبات من ملف requirements
if [ -f requirements.txt ]; then
    echo " [!] Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo " [!] requirements.txt not found! Installing manually..."
    pip install groq rich psutil
fi
echo -e "\n\033[1;32m [✓] Setup Complete! \033[0m"
echo -e "\033[1;34m [▶] To start the dragon, run: python ai_dragon.py \033[0m\n"

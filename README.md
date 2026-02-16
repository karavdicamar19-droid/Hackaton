     # 💀 GHOST AI V35.5 - BY AMAR IT-AI

![GHOST](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Language-Python-blue)

**GHOST** je napredni hakerski AI asistent integrisan u Termux. Koristi moć Gemini 3, 2.5 i 2.0 modela sa automatskom rotacijom ključeva.

## 🚀 Mogućnosti
- **Multi-Model Support:** Gemini 3 Flash, Pro, Gemma 3, i drugi.
- **Smart Rotation:** Ako jedan ključ "pukne" (429), Ghost sam uzima drugi.
- **Voice Output:** Ghost priča sa tobom na bosanskom jeziku.
- **Admin Panel:** Upravljanje ključevima i GitHubom preko `admin.py`.

## 🛠 Instalacija
```bash
[git clone [https://github.com/TVOJ-USER/GHOST-AI.git]](https://github.com/karavdicamar19-droid/Hackaton)
cd Hackaton
pip install -r requirements.txt
pkg install mpv -y
cp .env.example .env
pkg update && pkg upgrade -y
pkg install python git mpv multimedia-terminating-sound -y
pip install requests python-dotenv gTTS

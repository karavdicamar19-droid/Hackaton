import os, random
from dotenv import load_dotenv

# Učitavanje ključeva iz .env fajla
load_dotenv()

# 1. TVOJA LISTA MODELA (Poredana po snazi i stabilnosti)
MODELS_LIST = [
    "gemini-3-flash-preview",
    "gemini-3-pro-preview",
    "gemini-2.5-pro",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-exp-1206",
    "gemma-3-27b-it",
    "gemma-3-12b-it",
    "gemini-1.5-flash-latest",
    "gemini-pro-latest"
]

def get_clean_keys():
    """Čisti ključeve iz .env fajla i uklanja duplikate"""
    raw_keys = os.getenv("GHOST_KEYS", "")
    unique_keys = []
    seen = set()
    for k in raw_keys.split(","):
        clean_key = k.strip()
        if clean_key and clean_key not in seen and len(clean_key) > 20:
            unique_keys.append(clean_key)
            seen.add(clean_key)
    return unique_keys

# Inicijalizacija ključeva i indeksa
KEYS_LIST = get_clean_keys()
CURRENT_KEY_INDEX = 0
CURRENT_MODEL_INDEX = 0

def rotate_all():
    """Glavna funkcija za rotaciju: prvo mijenja ključ, pa model"""
    global CURRENT_KEY_INDEX, CURRENT_MODEL_INDEX
    if not KEYS_LIST:
        return
    
    # Pomjeri na sljedeći ključ
    CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(KEYS_LIST)
    
    # Ako smo napravili puni krug kroz sve ključeve, promijeni model
    if CURRENT_KEY_INDEX == 0:
        CURRENT_MODEL_INDEX = (CURRENT_MODEL_INDEX + 1) % len(MODELS_LIST)

def get_active_params():
    """Vraća trenutno aktivni ključ i model"""
    if not KEYS_LIST:
        return None, MODELS_LIST[CURRENT_MODEL_INDEX]
    return KEYS_LIST[CURRENT_KEY_INDEX], MODELS_LIST[CURRENT_MODEL_INDEX]

def get_profile():
    """Učitava tvoju biografiju i kreira sistemski profil"""
    biografija = ""
    if os.path.exists("bio.txt"):
        try:
            with open("bio.txt", "r", encoding="utf-8") as f:
                biografija = f.read().strip()
        except:
            biografija = "Vlasnik Paklene Bašte."
    
    return (
        "Ti si GHOST AI, elit

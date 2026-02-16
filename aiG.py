import config, requests, os, sys, json, time, subprocess
from gtts import gTTS

# Inicijalizacija memorije
chat_history = []

def ghost_speak(text):
    """Pretvara tekst u glas i reprodukuje ga u Termuxu"""
    try:
        # Čišćenje simbola radi boljeg izgovora
        clean_text = text.replace('*', '').replace('#', '').replace('_', '')
        tts = gTTS(text=clean_text, lang='bs')
        tts.save("odgovor.mp3")
        # mpv je najstabilniji plejer za Termux
        subprocess.run(["mpv", "--no-video", "odgovor.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove("odgovor.mp3")
    except Exception:
        pass # Ne dozvoli da audio greška sruši bot

def ghost_terminal_header():
    """Hakerski vizuelni identitet"""
    os.system('clear')
    print("\033[1;31m" + r"   ________  ______  ___________    ___    ____")
    print(r"  / ____/ / / / __ \/ ___/_  __/   /   |  /  _/")
    print(r" / / __/ /_/ / / / /\__ \ / /     / /| |  / /  ")
    print(r" / /_/ / __  / /_/ /___/ // /     / ___ |_/ /   ")
    print(r"\____//_/ /_/ \____/ /____//_/     /_/  |_/___/   " + "\033[0m")
    print(f"\033[1;32m[+] GHOST V35.5 | GITHUB EDITION | OWNER: AMAR IT-AI\033[0m")
    print(f"\033[1;90m[+] Sistemi: {len(config.KEYS_LIST)} ključeva | {len(config.MODELS_LIST)} modela\033[0m")
    print("\033[1;90m" + "─" * 60 + "\033[0m")

def ask_ghost():
    global chat_history
    ghost_terminal_header()
    profile = config.get_profile()

    while True:
        user_input = input("\n\033[1;31mUser@Ghost:~$ \033[0m").strip()
        
        if not user_input: continue
        if user_input.lower() in ['exit', 'quit', 'clear']:
            if user_input == 'clear': 
                chat_history = []
                ghost_terminal_header()
                continue
            break

        # Dodavanje korisničkog unosa u historiju (memoriju)
        chat_history.append({"role": "user", "parts": [{"text": user_input}]})
        
        # Limit memorije da se ne prepuni API request
        if len(chat_history) > 10: 
            chat_history = chat_history[-10:]

        success = False
        while not success:
            api_key, model_name = config.get_active_params()
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
            
            sys.stdout.write(f"\r\033[1;90m[*] Prodor -> Model: {model_name} | Key: {config.CURRENT_KEY_INDEX}\033[0m")
            sys.stdout.flush()

            try:
                payload = {
                    "contents": chat_history,
                    "system_instruction": {"parts": [{"text": profile}]}
                }
                
                # Slanje zahtjeva
                r = requests.post(url, json=payload, timeout=25)
                
                if r.status_code == 200:
                    sys.stdout.write("\r" + " " * 80 + "\r")
                    data = r.json()
                    
                    # Parsiranje odgovora
                    if 'candidates' in data and data['candidates']:
                        odgovor = data['candidates'][0]['content']['parts'][0]['text']
                        
                        # Spremanje u memoriju
                        chat_history.append({"role": "model", "parts": [{"text": odgovor}]})
                        
                        # Ispis i glas
                        print(f"\n\033[1;34m[ GHOST ]\033[0m\n{odgovor}")
                        ghost_speak(odgovor)
                        success = True
                    else:
                        config.rotate_all()
                        continue

                elif r.status_code == 429:
                    # Rate limit - previše zahtjeva, rotiraj odmah
                    config.rotate_all()
                    time.sleep(0.5)
                    continue
                
                elif r.status_code ==

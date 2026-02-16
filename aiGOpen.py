import requests
import os
import time

# --- VEZA SA AMAROVIM GHOST SERVEROM ---
# Ovaj link vodi direktno do Amara
SERVER_URL = "https://venture-much-tom-zones.trycloudflare.com/chat"

def main():
    os.system('clear')
    print("\033[1;31m")
    print(r"  ____ _   _  ___  ____ _____ ")
    print(r" / ___| | | |/ _ \/ ___|_   _|")
    print(r"| |  _| |_| | | | \___ \ | |  ")
    print(r"| |_| |  _  | |_| |___) || |  ")
    print(r" \____|_| |_|\___/|____/ |_|  ")
    print("\033[0m")
    print("\033[1;37m[ KLIJENT AKTIVAN ] Povezano na GHOST AI v3.0\033[0m")
    print("--------------------------------------------")
    print("Uputstvo: Kucaj poruku i pritisni Enter.")
    print("Za izlaz kucaj 'exit'.\n")
    
    while True:
        try:
            msg = input("\033[1;32mTi: \033[0m")
            
            if msg.lower() in ['exit', 'quit', 'izlaz']:
                print("Veza prekinuta.")
                break
                
            if not msg.strip():
                continue

            # Šalje poruku na tvoj Cloudflare tunel
            response = requests.post(
                SERVER_URL, 
                json={"message": msg},
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                # Odgovor tvog AI-a koji stiže sa tvog telefona
                print(f"\033[1;31mGHOST:\033[0m {data.get('ghost')}\n")
            elif response.status_code == 403:
                print("\033[1;31m[!] ZABRANJEN PRISTUP: Amar te je banovao!\033[0m\n")
            else:
                print(f"\033[1;33m[!] Greška na serveru (Status: {response.status_code})\033[0m\n")
                
        except requests.exceptions.ConnectionError:
            print("\033[1;31m[!] Server je ugašen ili nemaš internet.\033[0m\n")
        except Exception as e:
            print(f"\033[1;33m[!] Došlo je do greške: {e}\033[0m\n")

if __name__ == "__main__":
    # Provjera da li imaju instaliran requests
    try:
        main()
    except ImportError:
        print("Instaliraj biblioteku: pip install requests")

import os, sys, subprocess, time

def header():
    os.system('clear')
    print("\033[1;31m")
    print(r"   ______ __  ______  _____  ______")
    print(r"  / ____// / / / __ \/ ___/ /_  __/")
    print(r" / / __ / /_/ / / / /\__ \   / /   ")
    print(r"/ /_/ // __  / /_/ /___/ /  / /    ")
    print(r"\____//_/ /_/\____//____/  /_/     ")
    print("\033[1;32m[+] ADMIN CONTROL PANEL | OWNER: AMAR IT-AI\033[0m")
    print("\033[1;90m" + "─" * 45 + "\033[0m")

def run_cmd(cmd):
    """Izvršava sistemsku komandu i vraća status"""
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except:
        return False

def push_to_github():
    header()
    print("[*] Priprema za GitHub...")
    commit_msg = input("\033[1;37mUnesite opis promjena (Commit message): \033[0m")
    if not commit_msg: commit_msg = "Update GHOST V35.5"

    print("\n[*] Dodavanje fajlova...")
    run_cmd("git add .")
    
    print("[*] Kreiranje commita...")
    run_cmd(f'git commit -m "{commit_msg}"')
    
    print("[*] Slanje na server (Pushing)...")
    if run_cmd("git push origin main"):
        print("\033[1;32m\n[+] USPJEŠNO POSLANO NA GITHUB!\033[0m")
    else:
        print("\033[1;31m\n[!] GREŠKA PRI SLANJU. Provjeri internet ili GitHub token.\033[0m")
    time.sleep(2)

def manage_env():
    header()
    print("[1] Promijeni GHOST_KEYS (API Ključeve)")
    print("[2] Promijeni ADMIN_PW (Lozinku)")
    print("[3] Pogledaj trenutni .env")
    print("[B] Nazad")
    
    choice = input("\n\033[1;31mAdmin@Ghost:~$ \033[0m").lower()
    
    if choice == '1':
        keys = input("Zalijepi nove ključeve (odvojene zarezom): ")
        run_cmd(f'sed -i "s/^GHOST_KEYS=.*/GHOST_KEYS={keys}/" .env')
        print("[+] Ključevi ažurirani.")
    elif choice == '2':
        new_pw = input("Unesi novu ADMIN_PW: ")
        run_cmd(f'sed -i "s/^ADMIN_PW=.*/ADMIN_PW={new_pw}/" .env')
        print("[+] Lozinka ažurirana.")
    elif choice == '3':
        print("\n\033[1;33m--- TRENUTNI .ENV ---")
        os.system("cat .env")
        input("\n[Pritisni Enter za nazad]")

def main():
    while True:
        header()
        print("\033[1;37m[1] POKRENI GHOST AI (aiG.py)")
        print("[2] POŠALJI NA GITHUB (Git Push)")
        print("[3] UPRAVLJAJ KLJUČEVIMA (.env)")
        print("[4] PROVJERI UPDATE (Git Pull)")
        print("[0] IZLAZ\033[0m")
        
        choice = input("\n\033[1;31mAdmin@Ghost:~$ \033[0m")
        
        if choice == '1':
            os.system("python aiG.py")
        elif choice == '2':
            push_to_github()
        elif choice == '3':
            manage_env()
        elif choice == '4':
            header()
            print("[*] Provjeravam nove verzije...")
            run_cmd("git pull origin main")
            time.sleep(2)
        elif choice == '0':
            print("Gašenje Admin panela...")
            break

if __name__ == "__main__":
    main()

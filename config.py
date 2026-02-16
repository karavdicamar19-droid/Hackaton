   1 import os
 2
 3 # 1. TVOJI GEMINI KLJUČEVI
 4 def get_clean_keys():
 5     # Ovdje unesi svoj ključ unutar navodnika
 6     return ["AIzaSy...OVDE_ZALIJEPI_SVOJ_KLJUČ..."]
 7
 8 # 2. SISTEM ZA BAN_OVANJE
 9 def block_ip(ip):
10     if not ip or ip == "127.0.0.1": return
11     with open("blocked_ips.txt", "a") as f:
12         f.write(f"{ip}\n")
13
14 def is_blocked(ip):
15     if not os.path.exists("blocked_ips.txt"): return False
16     with open("blocked_ips.txt", "r") as f:
17         return ip in [line.strip() for line in f.readlines()]
18
19 # 3. LOGOVANJE RAZGOVORA
20 def log_chat(ip, msg, response):
21     from datetime import datetime
22     with open("chat_history.log", "a") as f:
23         vrijeme = datetime.now().strftime('%H:%M:%S')
24         f.write(f"[{vrijeme}] IP: {ip} | MSG: {msg} | AI: {response}\n")
25






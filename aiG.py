45     try:
46         r = requests.post(url, json={"contents": [{"parts": [{"text": user_msg}]}]})
47         odgovor = r.json()['candidates'][0]['content']['parts'][0]['text']
48
49         # 3. Glasovna potvrda na tvom telefonu
50         speak(odgovor)
51
52         return jsonify({"ghost": odgovor, "status": "delivered"})
53     except Exception as e:
54         return jsonify({"error": str(e)}), 500
55
56 if __name__ == "__main__":
57     # Server sluša na 8080 (Cloudflare tunel)
58     print("\n\033[1;32m[+] GHOST SERVIS JE ONLINE\033[0m")
59     print(f"[+] Link: https://venture-much-tom-zones.trycloudflare.com/chat")
60     app.run(host='0.0.0.0', port=8080)
61



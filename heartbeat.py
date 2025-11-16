import time
import requests

URL = "https://status.kaioaugusto.com/api/push/KEoXTMAwvImLkeCp6LVWFgrp1HmquhkO?status=up&msg=OK&ping="
INTERVAL = 20

while True:
    start = time.time()
    try:
        response = requests.get(URL, timeout=5)
        print(f"Heartbeat enviado. Código de status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ocorreu um erro: {e}")
    elapsed = time.time() - start
    sleep_time = max(0, INTERVAL - elapsed)
    time.sleep(sleep_time)

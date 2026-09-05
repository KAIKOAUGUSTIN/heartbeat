import time
import requests

URL = "https://status.kaioaugusto.com/api/push/zOH3vLimxVcRf7A4SH77mcDUWqVT9lkM?status=up&msg=OK&ping="
INTERVAL = 30

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

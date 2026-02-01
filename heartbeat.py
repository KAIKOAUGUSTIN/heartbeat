import time
import requests

URL = "https://uptime.betterstack.com/api/v1/heartbeat/j65Zh9SrEgMichFbPyuqjqnE"
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

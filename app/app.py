import requests
import time
from flask import Flask

app = Flask(__name__)

dns_servers = ["1.1.1.1", "8.8.8.8"]


def check_dns():
    while True:
        for server in dns_servers:
            try:
                requests.get(f"https://{server}", timeout=5)
                print(f"DNS server up {server}")
            except requests.ConnectionError:
                print(f"Dns server down {server}")
        time.sleep(5)


@app.route("/health")
def health_check():
    return "200 OK"


if __name__ == "__main__":

    import threading
    t = threading.Thread(target=check_dns)
    t.start()

    app.run(host="0.0.0.0", port=8080)

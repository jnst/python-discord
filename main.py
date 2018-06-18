import os
import sys
import requests

WEBHOOK_URL = os.getenv('WEBHOOK_URL')

def send(message):
    if not WEBHOOK_URL:
        print('error: must specify webhook url')
        sys.exit(1)

    payload = {'content': message}
    r = requests.post(WEBHOOK_URL, payload)
    r.raise_for_status
    print('success')

if __name__ == '__main__':
    send('hello, world')

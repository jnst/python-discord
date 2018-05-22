import requests

WEBHOOK_URL = 'https://discordapp.com/api/webhooks/xxxxxxxxxx'

def send(message):
    payload = {'content': message}
    requests.post(WEBHOOK_URL, payload)

send('hello')

import requests
import re

TOKEN = "8768491866:AAFMJmMx06G4Qw3H13dFPFybGiRHMX6mHBY"
CHAT_ID = "6154910185"

URL = "https://appointment.mosaicvisa.com/calendar/9"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

r = requests.get(URL).text

match = re.search(r"Reserved (\d+)", r)

if match:
    num = int(match.group(1))
    
    if num > 0:
        send(f"🚨 يوجد {num} موعد متاح الان\n{URL}")

import requests

TOKEN = "1393764739:AAHdgG7ehkUtXVkN14lzI9E73RRHTuxUrIU"

URL = "https://api.telegram.org/bot{token}/{method}"

updates = "getUpdates"  # getUpdates - метод для получения обновлений в telegram API

url = URL.format(token=TOKEN, method=updates)

# print(url)

response = requests.get(url)  # sending get-request
print(response)

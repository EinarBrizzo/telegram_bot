TOKEN = "1393764739:AAHdgG7ehkUtXVkN14lzI9E73RRHTuxUrIU"

URL = "https://api.telegram.org/bot{token}/{method}"
updates = "getUpdates"  # getUpdates - метод для получения обновлений в telegram API
send = "sendMessage" # метод для отправки данных. Название метода нужно брать из API
MY_ID = 141756366

with open("update_id.txt") as file:
    UPDATE_ID = file.readline()

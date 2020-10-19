import requests
import json
import const
import time
from pprint import pprint

def main ():
    while True:
        url = const.URL.format(token=const.TOKEN, method = const.updates)
        content = requests.get(url).text
        data = json.loads(content)
        result = data["result"][::-1]
        needed_part = None
        
        for element in result:
            if element["message"]["chat"][id] ==  const.MY_ID:
                needed_part = element
                break
        pprint(needed_part)
                 
        if not const.UPDATE_ID:
            with open("update_id.txt", "w") as file:
                file.write(str(needed_part["update_id"]))

        if const.UPDATE_ID != needed_part["update_id"]:
            pass

        pprint(data)
        time.sleep(2)


if __name__ == "__main__":
    main()



















#url_get = URL.format(token=TOKEN, method=updates)
#url_post = URL.format(token=TOKEN, method=send)

#data = {
   # "chat_id": "141756366", 
    #"text": "Hello from bot again"


#response_from_bot = requests.post(url_post, data=data)
#print(response_from_bot)
#print(response_from_bot.text)
# print(url)

#response = requests.get(url)  # sending get-request





#json_content = json.loads(response.text)

#print(json_content)
#print(response.text)
#print(type(json_content))

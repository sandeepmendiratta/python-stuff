
import requests
# print(python --version)
my_request = requests.get('http://go.codeschool.com/spamvanmenu')
menu_list = my_request.json()
print("Today's menu")
for item in menu_list:
    print(item['name'], ':', item['desc'].title(), item['price'])

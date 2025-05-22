import requests
import json
city = input()
api = "3389d389d797e76f84eaca19eb4fb4cc"
api_url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
rdata = requests.get(api_url)
data = rdata.json()
print(data)
for i in data["main"]:
    print(i["temp"])
import json

import requests

api_key = "46d6a53307e9d13813f5af71d1f8db3c"
url = "http://api.openweathermap.org/data/2.5/" "weather?units=metric&q={q}&appid={key}"

a = str(input("県名(ローマ字)をいれてください："))
city = a
url1 = url.format(q=city, key=api_key)
response = requests.get(url1)
data = response.json()

jsontext = json.dumps(data, indent=4)

print(jsontext)

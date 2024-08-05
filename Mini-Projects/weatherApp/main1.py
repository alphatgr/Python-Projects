import requests
import json
city=input("Enter the name of the city : \n")
url=f"https://api.weatherapi.com/v1/current.json?key=1ca6089887fa4a09a8f50116242902&q={city}"
r=requests.get(url)
print(r.text)
print(type(r.text))
wdic= json.loads(r.text)
print(wdic)
print(type(wdic))
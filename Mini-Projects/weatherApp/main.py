import requests
import json
import pyttsx3
engine=pyttsx3.init()

# RATE

rate = engine.getProperty('rate')
engine.setProperty('rate',150)

print("WELCOME TO THE WEATHER APP DESIGNED BY HAIDER ABBAS \n")
print("TO EXIT THE APP TYPE 'CLOSE APP' \n")
engine.say("WELCOME TO THE WEATHER APP DESIGNED BY HAIDER ABBAS")
engine.say("TO EXIT THE APP TYPE 'CLOSE APP'")
engine.runAndWait()
while True:
    try:
        engine.say("Enter the name of the city")
        engine.runAndWait()
        city=input("Enter the name of the city : \n")
        if city=="CLOSE APP" or city=="close app" or city=="exit" or city=="Exit" or city=="EXIT" or city=="Close app" or city=="Close App":
            engine.say("THANK YOU FOR USING THIS WEATHER APP")
            print("THANK YOU FOR USING THIS WEATHER APP")
            engine.runAndWait()
            break
        engine.say("Do you want the temperature in Celsius or Farenheit")
        engine.runAndWait()
        temp=input("Do you want the temperature in Celsius or Farenheit : \n")
        if temp=="CLOSE APP" or temp=="close app" or temp=="exit" or temp=="EXIT" or temp=="Exit" or temp=="Close app" or temp=="Close App":
            engine.say("THANK YOU FOR USING THIS WEATHER APP")
            print("THANK YOU FOR USING THIS WEATHER APP")
            engine.runAndWait()
            break
        url=f"https://api.weatherapi.com/v1/current.json?key=1ca6089887fa4a09a8f50116242902&q={city}"
        r=requests.get(url)
        # print(r.text)
        weather_dic=json.loads(r.text)
        if temp=='farenheit' or temp=='Farenheit' or temp=='f' or temp=='F' or temp=='FARENHEIT':
            # print(weather_dic["current"]["temp_f"])
            f=weather_dic["current"]["temp_f"]
            engine.say(f"The weather in {city} is {f} farenheit")
            print(f"The weather in {city} is {f} farenheit")
            engine.runAndWait()
        elif temp=='celsius' or temp=='Celsius' or temp=='c' or temp=='C' or temp=='CELSIUS':
            # print(weather_dic["current"]["temp_c"])
            c=weather_dic["current"]["temp_c"]
            engine.say(f"The weather in {city} is {c} degree celsius")
            print(f"The weather in {city} is {c} degree celsius")
            engine.runAndWait()
        else :
            print("Wrong Input")
        print("\n")
    except:
        engine.say("Sorry please recheck the city name that you have entered")
        engine.runAndWait()
        print("Sorry please recheck the city name that you have entered.")
import requests
api_key = 'bbcfd621f8689a0d174c292e0889afab'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
#print(weather_data.json())  #this will return the data that is in json format
if  weather_data.json()['cod'] =='404':
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    temp_cel = round((temp - 32) * 5 / 9)

    print(f"The weather in {user_input} is {weather}")
    print(f"The temperature in {user_input} is {temp_cel}")



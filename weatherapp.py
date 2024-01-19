import requests

api_key = '0633962c5221d60fdc0cea932c469417'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.status_code == 404:
    print("you can't type, bitch")
else:
    try:
        cod = weather_data.json()['cod']
        if cod == '404':
            print("you can't type, bitch")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            print(f"The weather in {user_input} is: {weather}")
            print(f"The temp in {user_input} is: {temp}-F")
    except KeyError:
        print("Error in the response format. Please try again later.")

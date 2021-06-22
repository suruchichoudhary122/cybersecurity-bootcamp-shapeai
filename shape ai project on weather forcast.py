import request
from datetime import datetime
api_key = '980da904b7730fea016c09b0b2c00c5f'

location = input("Enter city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

api_link = requests.get(complete_api_link)
api_data = api_link.json()
temp_city = ((api_data['main']['temp'])-273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %s | %I:%M:%S %p")
print("...............................................................")
print("weather starts for - {} || {}".format(location.upper(), datetime))
print("................................................................")


print("Current Temetrature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :",weather_desc)
print("Current humidity      :",hmdt, '%')
print("Curent wind speed     :",wind_spd , 'kmph')


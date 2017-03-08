import requests


print "Welcome to our cool weather console app" 

city = raw_input("Enter city name: ")

api_key = "077936f695f61908cd19a5a2452a97fb"

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}".format(city, api_key))

print response.json()



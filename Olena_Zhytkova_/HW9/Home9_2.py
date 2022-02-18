import pyowm


city=input('What sity are you interested: ')

owm=pyowm.OWM('2a1bd0c6ce804b7f7dcb5fab872d0a76')
mgr=owm.weather_manager()

observation=mgr.weather_at_place(city)
w=observation.weather
temperature=w.temperature('celsius')['temp']

print(f'In {city} city is the temperature of the air {temperature:>8} for the Celsius')
print('In this city ' + w.detailed_status)
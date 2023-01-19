import requests
import csv

# Map CSV file to obtain country latitude and longitude data
reader = csv.reader(open('code/countries.csv'))
countries = {}
for row in reader:
    country = row[0]
    if country in countries:
        pass
    countries[country.lower()] = row[1:]

def handle_user_msg(message):
    p_message = message.lower()
    if p_message.startswith('!weather'):
        return handle_weather_req(p_message.replace('!weather', ''))
    elif p_message == '!help':
        return "Please visit the following GitHub repo for more information:\nhttps://github.com/Pexers/docker-weather-forecast-bot"
    else: 
        return 'I don\'t know what that means. Try typing "!help".'

def handle_weather_req(message):
  response = ""
  api_url = 'https://api.open-meteo.com/v1/forecast'
  # Handle by country
  if message.startswith('/country'):
    country = message.split('/country/', 1)[1]
    # Verify if user inserted a valid country
    if country not in countries:
      return 'Country not found.'
    values = countries.get(country)
    api_url = api_url + '?latitude=$lat&longitude=$long&current_weather=true'
    api_url = api_url.replace('$lat', values[0]).replace('$long', values[1])
    # Make GET request to obtain weather data
    response = requests.get(url=api_url).json()
    # Read temperature from JSON response
    temperature = response.get('current_weather').get('temperature')
    return 'The current temperature in `' + country.upper() + '` is around ' + f'{temperature}°C.'
  return 'Command not found.'

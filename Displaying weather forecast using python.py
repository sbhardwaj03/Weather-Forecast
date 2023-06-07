import requests

#input the city name
cityname = input('input the city name')
print(cityname)
#Display the message!
print('Displaying Weather report for: ' + cityname)
#fetch the weater details
url = 'https://wttr.in/{}'.format(cityname)
result = requests.get(url)                       
#display the result!
print(result.text)

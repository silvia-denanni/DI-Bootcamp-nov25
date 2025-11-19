# API --> Application Programming Interface
# the way to ask for data and get it from the internet
import requests
import json 
import os

response = requests.get("https://api.chucknorris.io/jokes/random")

print(response)             #>>>   <Response [200]>

jokes_data = response.json()           # to see the data in JSON format
print(jokes_data)      # {'categories': [], 'created_at': '2020-01-05 13:42:25.352697', 'icon_url': 'https://api.chucknorris.io/img/avatar/chuck-norris.png', 'id': '1n-8CqniTlWWjQs1CYlQqw', 'updated_at': '2020-01-05 13:42:25.352697', 'url': 'https://api.chucknorris.io/jokes/1n-8CqniTlWWjQs1CYlQqw', 'value': "Chuck Norris' beard hair can be spun into gold. This is only in theory, for no one has, or 
                       #  will, ever touch Chuck's beard. EVER."}


jokes_data = response.json() 
print(jokes_data.get("value"))        # Throughout his life, Chuck Norris has been widely acknowledged and praised for the extreme realness with which he kept his shit.

#save the data in JSON file

dir_path = os.path.dirname(os.path.realpath(__file__))         

with open(dir_path + '\jokes.json', 'w') as f:
    json.dump(jokes_data, f, indent = 2, ensure_ascii = False)
    #print(type(jokes_data))                         #>>> <class 'dict'>
    print(jokes_data)


response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)   #>>> 200
print(response.text)          #>>>{"timestamp": 1763557266, "message": "success", "iss_position": {"longitude": "175.3605", "latitude": "9.7683"}}
print(response.json())        #>>> {'timestamp': 1763558326, 'message': 'success', 'iss_position': {'longitude': '-138.6789', 'latitude': '-40.5186'}}
print(type(response.json()))  #>>> <class 'dict'> ----------> THIS IS NOW A PYTHON DICTIONARY thanks to .json()

parameters = {"longitude": "175.3605", "latitude": "9.7683"}
response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)
iss_data = response.json()
print(iss_data[response][0])
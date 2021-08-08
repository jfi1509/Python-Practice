import requests
import ast

url = "https://maps.googleapis.com/maps/api/directions/json?origin=12.93175,77.62872&destination=12.92662,77.63696&key=AIzaSyAEQvKUVouPDENLkQlCF6AAap1Ze-6zMos"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

dict= ast.literal_eval(response.text)
legs_dict = dict["routes"][0]["legs"][0]

distance = 0
duration = 0
for leg in legs_dict:
    if(leg == 'steps'):
        directions_list = legs_dict[leg]
        for direction in directions_list:
            distance = distance + direction['distance']['value']
            duration = duration + direction['duration']['value']
            print(direction['distance']['value'],direction['duration']['value'])
            print(direction['start_location'], direction['end_location'])


print('{} kms, {} hours'.format(round(distance/1000.0,2), round(duration/3600.0,2)))


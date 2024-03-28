import json
import revgeo as revgeo

jsonfile = './jsonthing/file.json'

with open(jsonfile, 'r') as file:
    data = json.load(file)

    for node in data['salons_data']['data']['geolocation']['locations']['edges']:
        latitude = node['node']['address']['latitude']
        longitude = node['node']['address']['longitude']

        latitude_float = float(latitude)
        longitude_float = float(longitude)
        zipcode = revgeo.reverse_geocode(latitude_float,longitude_float)
        node['node']['address']['zipcode'] = zipcode
        print(latitude,longitude, zipcode)
        # print(node)

with open('filezipcode.json', 'w') as file:
    json.dump(data, file, indent=4)
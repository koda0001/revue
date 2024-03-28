import photon.revgeo1 as revgeo1
import csv

csv_file = "./cities_geocode_google2.csv"
with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(row[1])
        data = [row[1], row[2]]
        latitude_str = data[0]
        longitude_str = data[1]
        # Convert strings to floats
        latitude_float = float(latitude_str)
        longitude_float = float(longitude_str)
        #put me in scraper
        location = revgeo1.reverse_geocode(latitude_float,longitude_float)
        print("zip code is: ",location)

from geopy.geocoders import Photon
from geopy.exc import GeocoderTimedOut
import time
max_retries = 5
def reverse_geocode(lat, lon):
    geolocator = Photon(user_agent="geoapiExercises")
    for attempt in range(1, max_retries + 1):
        try:
            location = geolocator.reverse((lat, lon), exactly_one=True)

            address_details = location.raw.get('properties', {})
            time.sleep(2)
            zipcode = address_details.get('postcode')
            if zipcode:
                return zipcode
            else:
                return f"zipcode not found."
        except GeocoderTimedOut:
            return "Geocoder timed out. Please try again."
        except Exception as e:
            return f"An error occurred: {str(e)}"
            sleep_time = 5 * attempt
            print(f"Retrying in {sleep_time} seconds...")
            time.sleep(sleep_time)

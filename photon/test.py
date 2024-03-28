from geopy.geocoders import Photon
from geopy.exc import GeocoderTimedOut

def reverse_geocode(lat, lon, component=None):
    """
    Reverse geocode to get address details from latitude and longitude using the Photon geocoder.
    Optionally, extract a specific component from the address details.
    
    :param lat: Latitude of the location.
    :param lon: Longitude of the location.
    :param component: Optional. The specific component of the address to extract (e.g., 'postcode').
    :return: A string containing the full address, the specific address component if specified, or an error message.
    """
    geolocator = Photon(user_agent="geoapiExercises")

    try:
        location = geolocator.reverse((lat, lon), exactly_one=True)
        
        if not location:
            return "Location not found"
        
        address_details = location.raw.get('properties', {})  # Adjusted based on Photon's structure
        
        if component:
            # Attempt to extract and return the specified component.
            component_value = address_details.get(component)
            if component_value:
                return component_value
            else:
                return f"{component} not found."
        else:
            # If no specific component was requested, return the default address representation.
            return location.address
        
    except GeocoderTimedOut:
        return "Geocoder timed out. Please try again."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage:
lat = 48.8588443
lon = 2.2943506
print(reverse_geocode(lat, lon))  # Expected to print the full address
print(reverse_geocode(lat, lon, 'postcode'))  # Attempt to print just the postal code

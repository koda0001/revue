import requests

# You mentioned you have the API key, so make sure to replace 'YOUR_API_KEY_HERE' with your actual HERE API key.
API_KEY = ''
HERE_REVERSE_GEOCODE_URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"

def reverse_geocode(lat, lon):
    params = {
        'at': f'{lat},{lon}',
        'apikey': API_KEY,
    }
    
    try:
        response = requests.get(HERE_REVERSE_GEOCODE_URL, params=params)
        response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx
        data = response.json()
        
        # Parsing the response to extract the postal code
        address = data.get('items', [{}])[0].get('address', {})
        zipcode = address.get('postalCode')
        
        if zipcode:
            return zipcode
        else:
            return "Zipcode not found."
            
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

import requests

# Replace with your OpenRouteService API key
api_key = 'YOUR_API_KEY'

# Coordinates for start and end points
start_coords = (lat1, lon1)
end_coords = (lat2, lon2)

# URL for the OpenRouteService API
url = 'https://router.project-osrm.org/v2/directions/driving-car'

# Parameters for the API request
params = {
    'start': f'{start_coords[1]},{start_coords[0]}',
    'end': f'{end_coords[1]},{end_coords[0]}'
}

# Make the API request
response = requests.get(url, params=params)
data = response.json()

# Extract distance and route from response
distance = data['routes'][0]['summary']['distance']
route = data['routes'][0]['geometry']

print(f'Distance: {distance / 1000:.2f} km')
print(f'Route: {route}')

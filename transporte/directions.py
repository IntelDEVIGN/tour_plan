import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBbYU7-6GDjiGSWrpw5a1xKd1AUJMX5lnU')

map_directions = gmaps.directions('San Pedro Sula, Honduras', 'Copan Ruinas, Honduras', language='es')

print(map_directions[0]['legs'][0]['start_address'])
print(map_directions[0]['legs'][0]['end_address'])
print(map_directions[0]['legs'][0]['distance']['text'])
print(map_directions[0]['legs'][0]['distance']['value'])
print(map_directions[0]['legs'][0]['duration']['text'])
print(map_directions[0]['legs'][0]['duration']['value'])

for step in map_directions[0]['legs'][0]['steps']:
    print(step['html_instructions'])

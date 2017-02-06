import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBbYU7-6GDjiGSWrpw5a1xKd1AUJMX5lnU')

directions = gmaps.directions('San Pedro Sula, Honduras', 'Copan Ruinas, Honduras', language='es')
direcciones = directions[0]['legs'][0]

desde = direcciones['start_address']
hacia = direcciones['end_address']
distancia = direcciones['distance']['text']
distancia_v = direcciones['distance']['value']
duracion = direcciones['duration']['text']
duracion_v = direcciones['duration']['value']
steps = direcciones['steps']

print(desde)
print(hacia)
print(distancia)
print(distancia_v)
print(duracion)
print(duracion_v)

for step in steps:
    print(step['html_instructions'])

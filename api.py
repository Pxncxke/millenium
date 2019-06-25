import  requests

ship = "10/"
resp = requests.get("https://swapi.co/api/starships/"+ship)
print(resp.status_code)
data = resp.json()

print(str(data['name']))
print("Peliculas:")
for var in data['films']:
    url = str(var)
    pelis = requests.get(url)
    pelis = pelis.json()
    print(str(pelis['title']))
import requests

URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : '2afca6f92ecae67fae57fe743e201e97'}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 2
}
body_update = {
    "pokemon_id": "128820",
    "name": "Чармандер",
    "photo_id": 2
}
body_catch = {
    "pokemon_id": "128820"
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response_update.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

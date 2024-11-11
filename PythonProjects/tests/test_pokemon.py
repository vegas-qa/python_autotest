import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : '2afca6f92ecae67fae57fe743e201e97'}
TRAINER_ID = '9272'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    print(response)
    assert response.status_code == 200

def test_trainer_id():
    response_trainer_id = requests.get(url = f'{URL}/trainers',params = {'trainer_id' : TRAINER_ID})
    assert response_trainer_id.json()['data'][0]['id'] == TRAINER_ID


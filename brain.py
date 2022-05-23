"""Handle the requests for both APIs"""

from datetime import datetime
import os
import requests

Nutrix_ID = os.environ.get('NUTRIX_ID')
Nutrix_Key = os.environ.get('NUTRIX_KEY')
HEADER = {
    'x-app-id': Nutrix_ID,
    'x-app-key': Nutrix_Key,
    'Content-Type': 'application/json'
}
BASE_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
SHEETY_URL = os.environ.get('SHEETY_URL')


def get_data_form_nutrix(text):
    parameters = {
        "query": text,
        'gender': 'male',  # My infos
        'weight_kg': 93.5,  # My infos
        'height_cm': 181.98,  # My infos
        'age': 36  # My infos
    }
    response = requests.post(url=BASE_URL, headers=HEADER, json=parameters)
    return response.json()['exercises']


def post_row_to_sheets(a_list: list):
    for i in a_list:
        parameters = {
            'workout': {
                'date': datetime.now().strftime('%d/%m/%Y'),
                'time': datetime.now().strftime('%H:00:00'),
                'exercise': i['name'].title(),
                'duration': i['duration_min'],
                'calories': i['nf_calories']
            }
        }
        response = requests.post(url=SHEETY_URL, headers={
                                'Authorization': f'Bearer {SHEETY_TOKEN}',
                                'Content-Type': 'application/json'},
                                json=parameters)
        print(response.text)

# Base level script to interact with all GET endpoints for the API

import json
import requests

api_token = ''
api_url_base = 'https://api.wanikani.com/v2/'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def get_account_info():
    
    print('Endpoint options listed at https://docs.api.wanikani.com/20170710/')
    api_endpoint = input('Please provide valid endpoint: ')
    api_url = api_url_base + api_endpoint

    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    print(api_url)
    print(headers)

    if response.status_code == 200:
        print('You have sucessfully authenticated to wanikani API!')
        print(response.encoding)
        data = response.json()
        print(data)
    elif response.status_code == 400 or 404:
        print('[!] Error bad request')
    elif response.status_code == 500:
        print('[!] Error server error')
    else:
        print('[!] Request has Failed')

get_account_info()

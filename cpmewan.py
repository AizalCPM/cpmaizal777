# Source Generated with ShoaibxAmer Pycdc
# File: cpmewan.pyc (Python 3.11)

import requests
from time import sleep
BASE_URL: str = 'https://www.cpmewan.com/api'

class CPMEwan:
    
    def __init__(self = None, access_key = None):
        self.auth_token = None
        self.access_key = access_key

    
    def login(self = None, email = None, password = None):
        payload = {
            'account_email': email,
            'account_password': password }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/account_login''', params = params, data = payload)
        response_decoded = response.json()
        if response_decoded.get('ok'):
            self.auth_token = response_decoded.get('auth')
        return response_decoded.get('error')

    
    def register(self = None, email = None, password = None):
        payload = {
            'account_email': email,
            'account_password': password }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/account_register''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('error')

    
    def delete(self):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        requests.post(f'''{BASE_URL}/account_delete''', params = params, data = payload)

    
    def get_player_data(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/get_data''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded

    
    def set_player_rank(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/set_rank''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def get_key_data(self = None):
        params = {
            'key': self.access_key }
        response = requests.get(f'''{BASE_URL}/get_key_data''', params = params)
        response_decoded = response.json()
        return response_decoded

    
    def set_player_money(self = None, amount = None):
        payload = {
            'account_auth': self.auth_token,
            'amount': amount }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/set_money''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def set_player_coins(self = None, amount = None):
        payload = {
            'account_auth': self.auth_token,
            'amount': amount }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/set_coins''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def set_player_name(self = None, name = None):
        payload = {
            'account_auth': self.auth_token,
            'name': name }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/set_name''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def set_player_localid(self = None, id = None):
        payload = {
            'account_auth': self.auth_token,
            'id': id }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/set_id''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def set_player_plates(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/set_plates''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def get_player_car(self = None, car_id = None):
        payload = {
            'account_auth': self.auth_token,
            'car_id': car_id }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/get_car''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def delete_player_friends(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/delete_friends''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def unlock_w16(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/unlock_w16''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def unlock_horns(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/unlock_horns''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def disable_engine_damage(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/disable_damage''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def unlimited_fuel(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/unlimited_fuel''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def set_player_wins(self = None, amount = None):
        payload = {
            'account_auth': self.auth_token,
            'amount': amount }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/set_race_wins''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def set_player_loses(self = None, amount = None):
        payload = {
            'account_auth': self.auth_token,
            'amount': amount }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/set_race_loses''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def unlock_houses(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/unlock_houses''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def unlock_smoke(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/unlock_smoke''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def unlock_paid_cars(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/unlock_paid_cars''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def unlock_all_cars(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/unlock_all_cars''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def unlock_all_cars_siren(self = None):
        payload = {
            'account_auth': self.auth_token }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/unlock_all_cars_siren''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

    
    def account_clone(self = None, account_email = None, account_password = None):
        payload = {
            'account_auth': self.auth_token,
            'account_email': account_email,
            'account_password': account_password }
        params = {
            'key': self.access_key }
        response = requests.post(f'''{BASE_URL}/clone''', params = params, data = payload)
        response_decoded = response.json()
        return response_decoded.get('ok')

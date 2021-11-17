import json
import requests
import logging

from .actions import FACEBOOK_API

_logger = logging.getLogger(__name__)

def fb_get_profile(user_id=None, token=None):
    try:
        if not (token and user_id):
            raise Exception("Token y/o usuario messenger no existe(n)")
        response = requests.get(f'{FACEBOOK_API}/{user_id}?access_token={token}')
        return response.json()
    except requests.exceptions.RequestException as err:
        _logger.warning(f'OOps: Something Else {err}')
    except requests.exceptions.HTTPError as errh:
        _logger.warning(f'Http Error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        _logger.warning(f'Error Connecting: {errc}')
    except requests.exceptions.Timeout as errt:
        _logger.warning(f'Timeout Error {errt}') 
    
def fb_send_message(data=None, id_facebook=None, token=None):
    try:
        headers = {'Content-type': 'application/json'}
        values = {
            "recipient": {
                "id": f"{id_facebook}"
            },
            "message": {
                "text": data['message']
            },
        }
        response = requests.post(
            f"{FACEBOOK_API}/v12.0/me/messages?access_token={token}",
            data=json.dumps(values),
            headers=headers,
        )
        return response.json()
    except requests.exceptions.RequestException as err:
        _logger.warning(f'OOps: Something Else {err}')
    except requests.exceptions.HTTPError as errh:
        _logger.warning(f'Http Error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        _logger.warning(f'Error Connecting: {errc}')
    except requests.exceptions.Timeout as errt:
        _logger.warning(f'Timeout Error {errt}') 

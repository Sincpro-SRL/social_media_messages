import json
import requests

from .actions import FACEBOOK_API

def fb_get_profile(user_id=None, token=None):
    if not (token and user_id):
        raise Exception("Token y/o usuario messenger no existe(n)")
    response = requests.get(f'{FACEBOOK_API}/{user_id}?access_token={token}')
    return response.json()
    
def fb_send_message(data=None, id_facebook=None, token=None):
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

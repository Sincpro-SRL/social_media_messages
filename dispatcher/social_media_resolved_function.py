import json
import requests

from .actions import FACEBOOK_API

def fb_get_profile(**kargs):
    user_id = kargs['USER_ID']
    token = kargs['TOKEN']
    if not (token and user_id):
        raise Exception("Token y/o usuario messenger no existe(n)")
    response = requests.get(f'{FACEBOOK_API}/{user_id}?access_token={token}')
    return response.json()
    
def fb_send_message(**kargs):
    data = kargs['DATA']
    id_facebook = kargs['FB_ID']
    token = kargs['TOKEN']
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

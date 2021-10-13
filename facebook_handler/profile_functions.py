import requests
from dataclasses import dataclass
FACEBOOK_API = 'https://graph.facebook.com'
@dataclass
class FacebookProfile:
    first_name: str 
    last_name: str
    facebook_user_id: str

def get_info_profile(user, token) :
    user_id = user["sender"]["id"]
    if not token and not user_id:
        raise Exception("Token y usuario invalidos")
    
    profile = requests.get(f'{FACEBOOK_API}/{user_id}?access_token={token}')
    
    facebook_response = profile.json()
    
    result = FacebookProfile(facebook_response["first_name"], facebook_response["last_name"], facebook_response["id"])
    print(facebook_response)
    return facebook_response

   
     

    
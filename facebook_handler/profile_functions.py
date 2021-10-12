import requests
from odoo.exceptions import ValidationError
from odoo.exceptions import AccessDenied

def get_info_profile(user, token):
    user_id = user["sender"]["id"]

    try:
        if not token:
            print("Error")
        else: 
            url = f'https://graph.facebook.com/{user_id}?access_token={token}'
            response = requests.get(url)
            return response.json()
    except:
        print("error")

    
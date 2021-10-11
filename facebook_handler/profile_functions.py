import requests
from . import get_token

def get_info_profile(user):
    user_id = user["sender"]["id"]

    token = get_token()
    if not token:
        return Response(status=404)
    else:
        url = f'https://graph.facebook.com/{user_id}?access_token={token}'
        response = requests.get(url)
        return response.json()

    
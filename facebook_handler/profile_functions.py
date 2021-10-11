import requests
from . import get_token

def get_info_profile(user):
    token = get_token()
    if not token:
        return Response(status=404)
    else:
        url = f'https://graph.facebook.com/{user}?access_token={token}'
        response = requests.get(url)
    print(response.json())

    
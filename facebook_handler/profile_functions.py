import requests

def get_info_profile(user, token):
    user_id = user["sender"]["id"]

    if not token:
        return token
    else:
        url = f'https://graph.facebook.com/{user_id}?access_token={token}'
        response = requests.get(url)
        return response.json()

    
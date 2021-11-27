from ..dispatcher.dispatcher import dispatch
from ..dispatcher.actions import FB_GET_PROFILE
from ..models.constants import FACEBOOK, RECEIVED


def fb_message_details_parser(data):
    entry = data["entry"][0]
    messaging = entry["messaging"][0]
    id = messaging["sender"]["id"]
    message_details = {
        "time": entry["time"],
        "page_id": entry["id"],
        "message": messaging["message"]["text"],
        "social_network": FACEBOOK,
        "status_message": RECEIVED,
    }
    return id, message_details


def fb_user_profile_parser(id, token):
    user_profile = dispatch(FB_GET_PROFILE, user_id=id, token=token)
    return {
        "first_name": user_profile["first_name"],
        "last_name": user_profile["last_name"],
        "id": user_profile["id"],
    }

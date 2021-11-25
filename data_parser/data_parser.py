from ..models.constans import FACEBOOK, RECEIVED


def fb_message_details_parser(data):
    entry = data["entry"][0]
    messaging = entry["messaging"][0]
    return {
        "time": entry["time"],
        "page_id": entry["id"],
        "customer_id": messaging["sender"]["id"],
        "message": messaging["message"]["text"],
        "social_network": FACEBOOK,
        "status_message": RECEIVED,
    }

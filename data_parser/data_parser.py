def fb_message_parser(data):
    entry_data = data["entry"][0]
    messaging = entry_data["messaging"][0]
    return {
        "time": entry_data["time"],
        "page_id": entry_data["id"],
        "customer_id": messaging["sender"]["id"],
        "customer_message": messaging["message"]["text"],
        "social_network": data["source"]["social_network"],
        "status_message": data["source"]["status_message"],
    }

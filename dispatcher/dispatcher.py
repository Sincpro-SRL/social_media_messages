from .social_media_dispatch import fb_get_profile, fb_send_message

from ..models.constant import FB_GET_PROFILE, FB_SEND_MESSAGE

dispatcher = {
    FB_SEND_MESSAGE: fb_send_message,
    FB_GET_PROFILE: fb_get_profile
}

def dispatch(action, **kargs):
    try:
        dispatcher[action](kargs)
    except:
        print('Error key Action')

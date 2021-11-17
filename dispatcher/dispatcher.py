import logging

from .social_media_resolved_function import fb_get_profile, fb_send_message

from .actions import FB_GET_PROFILE, FB_SEND_MESSAGE

_logger = logging.getLogger(__name__)

dispatcher = {
    FB_SEND_MESSAGE: fb_send_message,
    FB_GET_PROFILE: fb_get_profile
}

def dispatch(action, **kwargs):
    try:
        return dispatcher[action](**kwargs)
    except KeyError as err:
        _logger.warn('Key Error: Action no defined in the dispathcer module {err}')
    except BaseException as err:
        _logger.warning(f'OOps: Unexpected Error {err}')

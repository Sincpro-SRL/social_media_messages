# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import Response
import logging
#from ..facebook_handler.profile_functions import get_info_profile

_logger = logging.getLogger(__name__)

def get_info_profile():
    return "mensaje"

class ControllerWebhookMessenger(http.Controller):

    @http.route('/webhook_messenger', methods=['POST'], type='json', auth="public", csrf=False)
    def webhook(self, **kw):
        data = request.jsonrequest
        if data["object"] == "page":
            for info in data["entry"]:
                _logger.info(info["messaging"][0])
                profile_info = get_info_profile(info["messaging"][0], token)
                _logger.info(profile_info)
            return "EVENT_RECEIVED"
            
        else:
            return Response(status=404)

    @http.route('/webhook_messenger', methods=['GET'], auth="public")
    def verificacion_webhook(self, **kw):
        VERIFY_TOKEN = "Hola_mundo"

        data = request
        mode = data.params["hub.mode"]
        token = data.params["hub.verify_token"]
        challenge = data.params["hub.challenge"]

        if mode and token:
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                _logger.info('WEBHOOK_VERIFIED')
                return challenge
            else:
                return Response(status=403)

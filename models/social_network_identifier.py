import logging

from odoo import models, api

from ..data_parser.data_parser import fb_message_parser
from ..dispatcher.dispatcher import dispatch
from ..dispatcher.actions import FB_GET_PROFILE

FACEBOOK = "Facebook"


class SocialNetworkIdentifier(models.Model):
    _name = "social.metwork.identifier"
    _description = "Identifer data from Social Media"

    @api.model
    def identifier(self, social_identifier, **kwargs):
        social_network_handler = {
            FACEBOOK: self.facebook,
        }
        social_network = social_network_handler[social_identifier]
        social_network(**kwargs)

    def facebook(self, data=None):
        res_partner = self.env["res.partner"]
        management_data = self.env["management.data"]
        message = fb_message_parser(data)
        user_facebook = dispatch(FB_GET_PROFILE, user_id=message["customer_id"])
        message["contact"] = res_partner.create_social_network_contact(**user_facebook)
        social_media_message = management_data.storage_data(**message)

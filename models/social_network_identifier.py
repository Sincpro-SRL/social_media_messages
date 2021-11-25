import logging

from odoo import models, api

from ..data_parser.data_parser import fb_message_details_parser
from ..dispatcher.dispatcher import dispatch
from ..dispatcher.actions import FB_GET_PROFILE
from .constans import FACEBOOK


class SocialNetworkIdentifier(models.Model):
    _name = "social.network.identifier"
    _description = "Identifer data from Social Media"

    @api.model
    def identifier(self, social_identifier, **kwargs):
        social_network_handler = {
            FACEBOOK: self.facebook_handler,
        }
        social_network = social_network_handler[social_identifier]
        social_network(**kwargs)

    def facebook_handler(self, data=None):
        res_partner = self.env["res.partner"]
        management_data = self.env["management.data"]
        token = self.env["ir.config_parameter"].get_param("facebook.facebook_token")
        message_details = fb_message_details_parser(data)
        user_profile = dispatch(
            FB_GET_PROFILE, user_id=message_details["customer_id"], token=token
        )
        message_details["contact"] = res_partner.create_social_network_contact(
            user_profile
        ).id
        social_media_message = management_data.storage_data(message_details)

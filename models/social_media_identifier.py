from odoo import models, api

from ..data_parser.data_parser import fb_message_details_parser, fb_user_profile_parser
from .constants import FACEBOOK, SENT, NOT_SENT


class SocialMediaIdentifier(models.Model):
    _name = "social.media.identifier"
    _description = "Identifier data from Social Media"

    @api.model
    def identifier(self, id_social_media, **kwargs):
        social_media_handler = {
            FACEBOOK: self.facebook_handler,
        }
        social_media = social_media_handler[id_social_media]
        social_media(**kwargs)

    def facebook_handler(self, data=None):
        res_partner = self.env["res.partner"]
        social_media_messages = self.env["social.media.messages"]
        token = self.env["ir.config_parameter"].get_param("facebook.facebook_token")
        id, message_details = fb_message_details_parser(data)
        user_profile = fb_user_profile_parser(id, token)
        contact = res_partner.create_social_media_contact(**user_profile)
        social_media_messages.storage_message(contact.id, **message_details)

    @api.model
    def odoo_message_handler(self, data):
        social_media_messages = self.env["social.media.messages"]
        if data["response"]:
            data["status_message"] = SENT
        else:
            data["status_message"] = NOT_SENT

        social_media_messages.storage_message(**data)


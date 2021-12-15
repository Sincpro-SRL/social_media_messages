from odoo import models, api

from ..data_parser.data_parser import fb_message_details_parser, fb_user_profile_parser
from .constants import FACEBOOK


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
        opportunity_manager = self.env["opportunity.manager"]
        id, message_details = fb_message_details_parser(data)
        facebook_id = self.env["social.media.tokens"].search(
            [("page_id", "=", message_details["page_id"])]
        )
        user_profile = fb_user_profile_parser(id, facebook_id.token)
        contact = res_partner.create_social_media_contact(**user_profile)
        message = social_media_messages.storage_message(contact.id, **message_details)
        opportunity_manager.opportunity_handler(message)

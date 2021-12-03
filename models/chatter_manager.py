from datetime import datetime
import logging

from odoo import models, api, fields

from ..dispatcher.dispatcher import dispatch
from ..dispatcher.actions import FB_SEND_MESSAGE
from .constants import FACEBOOK

_logger = logging.getLogger(__name__)


class Chatter_manager(models.Model):
    _name = "chatter.manager"
    _description = (
        "Management the processes to send message from opportunity to social media"
    )

    note = fields.Text("Note")

    def chatter_handler(self):
        opportunity = self.env["crm.lead"].search(
            [("id", "=", self.env.context["default_res_id"])]
        )
        contact = opportunity.partner_id
        status = self.send_message_handler(contact)
        message = self.storage_message(contact, status)
        self.env["opportunity.manager"].message_post(opportunity, message)

    def send_message_to_facebbok(self, contact):
        token = self.env["ir.config_parameter"].get_param("facebook.facebook_token")
        return dispatch(
            FB_SEND_MESSAGE,
            message=self.note,
            id_facebook=contact.id_social_media,
            token=token,
        )

    def send_message_handler(self, contact):
        send_message = {FACEBOOK: self.send_message_to_facebbok}
        return send_message[contact.social_media](contact)

    def storage_message(self, contact, status):
        values = {
            "message": self.note,
            "contact": contact.id,
            "time": datetime.today(),
            "status_message": status,
            "social_network": contact.social_media,
        }
        return self.env["social.media.messages"].storage_message(**values)

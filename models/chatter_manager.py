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
        status = self.send_message_handler(contact, opportunity.page_id)
        message = self.storage_message(contact, status, opportunity.page_id)
        self.env["opportunity.manager"].message_post(opportunity, message)

    def send_message_to_facebbok(self, contact, page_id):
        token = self.env["facebook.page.id"].search([("page_id", "=", page_id)]).token
        return dispatch(
            FB_SEND_MESSAGE,
            message=self.note,
            id_facebook=contact.id_social_media,
            token=token,
        )

    def send_message_handler(self, contact, page_id):
        send_message = {FACEBOOK: self.send_message_to_facebbok}
        return send_message[contact.social_media](contact, page_id)

    def storage_message(self, contact, status, page_id):
        values = {
            "message": self.note,
            "contact": contact.id,
            "time": datetime.today(),
            "status_message": status,
            "social_network": contact.social_media,
            "page_id": page_id,
        }
        return self.env["social.media.messages"].storage_message(**values)

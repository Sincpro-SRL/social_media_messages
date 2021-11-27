import logging
from dataclasses import dataclass
from datetime import datetime, timedelta

from odoo import models, api, fields

from ..dispatcher.dispatcher import dispatch
from ..dispatcher.actions import FB_GET_PROFILE, FB_SEND_MESSAGE

_logger = logging.getLogger(__name__)


@dataclass
class FacebookProfile:
    first_name: str
    last_name: str
    id: str
    message: str


class CreateContactMessenger(models.Model):
    _name = "create.contact"
    _description = "Creacion de contacto apartir del evento del Webhook de messenger"
    _auto = False

    @api.model
    def create_partner_webhook_event(self, user):
        res_partner = self.env["res.partner"]
        values = {
            "name": f"{user.first_name} {user.last_name}",
            "id_facebook": user.id,
            "from_messenger": True,
        }
        return res_partner.create(values)


class FacebookHandler(models.Model):
    _name = "facebook.handler"
    _description = "Maneja datos de un perfil de usuario de facebook"

    note = fields.Text("Note")

    def get_messaging_data(self, entry_data):
        for information in entry_data:
            for key, value in information.items():
                if key == "messaging":
                    return value[0]
        return None

    @api.model
    def data_handler(self, data):
        token = self.env["ir.config_parameter"].get_param("facebook.facebook_token")
        message_info = self.get_messaging_data(data["entry"])
        user_id = message_info["sender"]["id"]
        user_profile = dispatch(FB_GET_PROFILE, user_id=user_id, token=token)
        return FacebookProfile(
            user_profile["first_name"],
            user_profile["last_name"],
            user_profile["id"],
            message_info["message"]["text"],
        )

    def send_message(self):
        token = self.env["ir.config_parameter"].get_param("facebook.facebook_token")
        crm_id_opportunity = self.env.context["default_res_id"]
        message = self.note
        opportunity = self.env["crm.lead"].search([("id", "=", crm_id_opportunity)])
        contact = opportunity.partner_id
        id_facebook = contact.id_facebook,
        response = dispatch(
            FB_SEND_MESSAGE,
            data=message,
            id_facebook=id_facebook,
            token=token,
        )
        values = {
            "response": response,
            "message": message,
            "contact": contact,
            "id_facebook": id_facebook,
            "time": datetime.today(),
        }
        self.env["social.media.messages"].odoo_message_handler(values)
        opportunity.message_post(body=f"Messenger: {message}")


class CrmManager(models.Model):
    _name = "crm.manager"
    _description = "Management the processes to create and verify an opportunity in CRM"
    _auto = False

    def verify_opportunity(self, crm_lead, name_opportunity):
        opportunity = crm_lead.search([("name", "=", name_opportunity)])
        if opportunity["name"] == name_opportunity:
            created_datetime = opportunity["create_date"]
            time_change = created_datetime + timedelta(days=7)
            today = datetime.today()
            if time_change >= today:
                return opportunity
        return None

    @api.model
    def create_opportunity(self, user, message):
        crm_lead = self.env["crm.lead"]
        name = f'{user["name"]}\'s opportunity Facebook'
        opportunity = self.verify_opportunity(crm_lead, name)
        if not opportunity:
            opportunity = crm_lead.create(
                {
                    "priority": "1",
                    "name": name,
                    "partner_id": user["id"],
                    "type": "opportunity",
                    "from_messenger_opportunity": True,
                }
            )
            _logger.info(f"New opportunity created: {name}")
        opportunity.message_post(body=message, message_type="comment")


class DataProcessor(models.Model):
    _name = "data.processor"
    _description = "Data processor about message of webhook facebook messenger"
    _auto = False

    @api.model
    def data_checker(self, data):
        user = self.env["facebook.handler"].data_handler(data)
        user_res_partner = self.user_checker(user.id)
        if not user_res_partner:
            user_res_partner = self.env["create.contact"].create_partner_webhook_event(user)
        _logger.info(user.message)
        self.env["crm.manager"].create_opportunity(user_res_partner, user.message)

    def user_checker(self, user_id):
        rest_partner = self.env["res.partner"]
        user = rest_partner.search([("id_facebook", "=", user_id)])
        if not user["id_facebook"] == user_id:
            return None
        return user

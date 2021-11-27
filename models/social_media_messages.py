from datetime import datetime
from odoo import models, fields, api


class SocialMediaMessages(models.Model):
    _name = "social.media.messages"
    _description = "Almacenamiento de información del mensaje"

    page_id = fields.Char(string="ID de la página receptora")
    customer_message = fields.Char(string="Mensaje de cliente")
    date_message = fields.Datetime(string="Fecha del mensaje recibido")
    social_network = fields.Char(string="Red social del mensaje")
    status_message = fields.Char(string="Estado del mensaje")
    attempts = fields.Integer(string="Número de intentos de envío")
    file_attached = fields.Binary(string="Archivo adjunto")
    contact = fields.Many2one("res.partner", string="Contacto Asociado al mensaje")

    @api.model
    def storage_message(
        self,
        contact,
        page_id=None,
        time=None,
        message=None,
        social_network=None,
        status_message=None,
    ):
        values = {
            "page_id": page_id,
            "date_message": datetime.utcfromtimestamp(time / 1000).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "customer_message": message,
            "social_network": social_network,
            "status_message": status_message,
            "attempts": 0,
            "file_attached": None,
            "contact": contact,
        }
        return self.create(values)

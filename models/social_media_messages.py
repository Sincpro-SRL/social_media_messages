# -*- coding: utf-8 -*
from datetime import datetime
from odoo import models, fields, api


class ManagementData(models.Model):
    _name = "management.data"
    _description = "Almacenamiento de información del mensaje"

    page_id = fields.Integer(string="ID de la página receptora", require=True)
    customer_message = fields.Char(string="Mensaje de cliente", require=True)
    date_message = fields.Date(string="Fecha del mensaje recibido", require=True)
    social_network = fields.Char(string="Red social del mensaje", require=True)
    status_message = fields.Char(string="Estado del mensaje", require=True)
    attempts = fields.Integer(string="Número de intentos de envío")
    file_attached = fields.Binary(string="Archivo adjunto")
    contact = fields.Many2one(
        "res.partner", string="Contacto Asociado al mensaje", require=True
    )

    @api.model
    def storage_data(
        self,
        page_id=None,
        time=None,
        message=None,
        social_network=None,
        status_message=None,
        contact=None,
    ):
        values = {
            "page_id": page_id,
            "date_message": datetime.utcfromtimestamp(time / 1000).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "customer_message": message,
            "social_network": social_network,
            "status_message": status_message,
            "attempts": None,
            "file_attached": None,
            "contact": contact,
        }
        return self.create(values)

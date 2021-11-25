# -*- coding: utf-8 -*
from datetime import datetime
from odoo import models, fields, api


class ManagementData(models.Model):
    _name = "management.data"
    _description = "Almacenamiento de información del mensaje"

    page_id = fields.Char(string="ID de la página receptora")
    customer_message = fields.Char(string="Mensaje de cliente")
    date_message = fields.Date(string="Fecha del mensaje recibido")
    social_network = fields.Char(string="Red social del mensaje")
    status_message = fields.Char(string="Estado del mensaje")
    attempts = fields.Integer(string="Número de intentos de envío")
    file_attached = fields.Binary(string="Archivo adjunto")
    contact = fields.Many2one("res.partner", string="Contacto Asociado al mensaje")

    @api.model
    def storage_data(self, data):
        values = {
            "page_id": data["page_id"],
            "date_message": datetime.utcfromtimestamp(data["time"] / 1000).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "customer_message": data["message"],
            "social_network": data["social_network"],
            "status_message": data["status_message"],
            "attempts": 0,
            "file_attached": None,
            "contact": data["contact"],
        }
        return self.create(values)

# -*- coding: utf-8 -*
from datetime import datetime
from odoo import models, fields


class ManagementData(models.Model):
    _name = 'management.data'
    _description = "Almacenamiento de información del mensaje"

    def storage_data(self, **kwargs):
        values = {
            'page_id': kwargs['page_id'],
            'customer_id': kwargs['customer_id'],
            'date_message': datetime.utcfromtimestamp(kwargs['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S'),
            'customer_message': kwargs['message'],
            'social_network': kwargs['social_network'],
            'status_message': kwargs['status_message'],
            'attempts': None,
            'file_attached': None,
            'contact': kwargs['contact'],
        }
        self.create(values)
        return "REGISTRO GUARDADO EXITOSAMENTE"

    page_id = fields.Integer(string="ID de la página receptora", required=True)
    customer_id = fields.Integer(string="ID de usuario de Facebook", required=True)
    customer_message = fields.Char(string="Mensaje de cliente", required=True)
    date_message = fields.Date(string="Fecha del mensaje recibido", required=True)
    social_network = fields.Char(string="Red social del mensaje", required=True)
    status_message = fields.Char(string="Estado del mensaje", required=True)
    attempts = fields.Integer(string="Número de intentos de envío")
    file_attached = fields.Binary(string="Archivo adjunto")
    contact = fields.Many2one("res.partner", string="Contacto Asociado al mensaje", required=True)



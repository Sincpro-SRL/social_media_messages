# -*- coding: utf-8 -*
from datetime import datetime
from odoo import models, fields, api


class HandlerMessenger(models.Model):
    _name = 'handler.messenger'
    _description = "Manejador de información messenger Webhook"

    def handler_body(self, data):
        entry_data = data['entry'][0]
        messaging = entry_data['messaging'][0]
        values = {
            'date_message': datetime.utcfromtimestamp(entry_data['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S'),
            'page_id': entry_data['id'],
            'customer_id': messaging['sender']['id'],
            'customer_message': messaging['message']['text'],
        }
        self.create(values)

    page_id = fields.Integer(string="ID de la página receptora")
    customer_id = fields.Integer(string="ID de usuario de Facebook")
    customer_message = fields.Char(string="Mensaje de cliente")
    date_message = fields.Date(string="Fecha del mensaje recibido")



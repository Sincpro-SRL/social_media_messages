# -*- coding: utf-8 -*
from datetime import datetime
from odoo import models, fields, api


class HandlerMessenger(models.Model):
    _name = 'handler.messenger'
    _description = "Manejador de información messenger Webhook"

    def handler_body(self, data):
        """
        :param data:
            {
                'object': 'page',
                'entry': {},
                'source': {
                    'social_network': Red social de la cual es recibido o enviado el mensaje,
                    'status_message': Estado del mensaje (RECEIVED, SENT, NO_SENT)
                },
                'attempts': Cantidad de intentos para enviar mensajes (re-sender),
                'file_attached': Archivo adjunto al mensaje,
            }
        :return:
            "REGISTRO CREADO EXITOSAMENTE"
        """

        entry_data = data['entry'][0]
        messaging = entry_data['messaging'][0]
        values = {
            'date_message': datetime.utcfromtimestamp(entry_data['time'] / 1000).strftime('%Y-%m-%d %H:%M:%S'),
            'page_id': entry_data['id'],
            'customer_id': messaging['sender']['id'],
            'customer_message': messaging['message']['text'],
            'social_network': data['source']['social_network'],
            'status_message': data['source']['status_message'],
            'attempts': None,
            'file_attached': None,
        }
        self.create(values)
        return "REGISTRO CREADO EXITOSAMENTE"

    page_id = fields.Integer(string="ID de la página receptora", require=True)
    customer_id = fields.Integer(string="ID de usuario de Facebook", require=True)
    customer_message = fields.Char(string="Mensaje de cliente", require=True)
    date_message = fields.Date(string="Fecha del mensaje recibido", require=True)
    social_network = fields.Char(string="Red social del mensaje", require=True)
    status_message = fields.Char(string="Estado del mensaje", require=True)
    attempts = fields.Integer(string="Número de intentos de envío")
    file_attached = fields.Binary(string="Archivo adjunto")



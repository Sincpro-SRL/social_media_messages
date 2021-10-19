# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AddIdFacebook(models.Model):
    _inherit = 'res.partner'

    id_facebook = fields.Char('ID perfil Facebook', readonly=True)
    from_messenger = fields.Boolean('Obtenido desde messenger', readonly=True)


class CreateContactMessenger(models.Model):
    _name = 'create.contact'
    _description = 'Creacion de contacto desde el Webhook de messenger'
    _auto = False

    @api.model
    def create_partner_webhook_event(self, dic_data):
        values = {
            'name': f"{dic_data['first_name']} {dic_data['last_name']}",
            'id_facebook': dic_data['id'],
            'from_messenger': True
        }
        self.env['res.partner'].create(values)

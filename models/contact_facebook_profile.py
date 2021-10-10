# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AddInfoProfile(models.Model):
    _inherit = 'res.partner'

    ID_facebook = fields.Char('ID perfil Facebook')

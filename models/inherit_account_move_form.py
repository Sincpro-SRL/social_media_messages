from odoo import api, fields, models

class AccountMoveForm(models.Model):
    _name = 'account.move'
    _inherit = ['account.move', 'sincpro.whatsapp']

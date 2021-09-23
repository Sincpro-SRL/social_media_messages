from odoo import fields, models

class WhatsappSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    note = fields.Char(string="Default Note")

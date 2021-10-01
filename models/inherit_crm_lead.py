from odoo import api, fields, models


class InheritCRMLead(models.Model):
    _name = 'crm.lead'
    _inherit = ['crm.lead', 'sincpro.whatsapp']

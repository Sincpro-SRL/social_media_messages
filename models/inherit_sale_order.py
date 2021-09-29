from odoo import api, fields, models


class InheritSaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order', 'sincpro.whatsapp']
    
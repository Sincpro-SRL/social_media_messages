from odoo import api, fields, models


class InheritCRMLead(models.Model):
    _name = 'crm.lead'
    _inherit = ['crm.lead', 'sincpro.whatsapp']

    from_messenger = fields.Boolean('Creado desde messenger', readonly=True, default=False)

    @api.model
    def get_data_from_model(self):
        return "Testing from Python"

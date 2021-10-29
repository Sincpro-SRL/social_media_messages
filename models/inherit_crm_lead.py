from odoo import api, fields, models


class InheritCRMLead(models.Model):
    _name = 'crm.lead'
    _inherit = ['crm.lead', 'sincpro.whatsapp']

    from_messenger_opportunity = fields.Boolean('Creado desde messenger', readonly=True, default=False)

    @api.model
    def get_data_from_model(self, id):
        data_from_messenger = self.search([('id', '=', id)])
        print(data_from_messenger)
        return data_from_messenger

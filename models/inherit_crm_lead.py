from odoo import api, fields, models


class InheritCRMLead(models.Model):
    _name = 'crm.lead'
    _inherit = ['crm.lead', 'sincpro.whatsapp']

    from_messenger_opportunity = fields.Boolean('Creado desde messenger', readonly=True, default=False)

    @api.model
    def get_data_from_model(self, id_opportunity):
        value = self.search([('id', '=', id_opportunity)]).from_messenger_opportunity
        print(value)
        return {
            "id_opportunity": id_opportunity,
            "from_messenger": value,
        }

from odoo import api, fields, models


class InheritCRMLead(models.Model):
    _inherit = "crm.lead"

    from_messenger_opportunity = fields.Boolean(
        "Creado desde messenger", readonly=True, default=False
    )
    page_id = fields.Char(string="ID de la página receptora")

    @api.model
    def get_data_from_model(self, id_opportunity):
        value = self.search([("id", "=", id_opportunity)]).from_messenger_opportunity
        return {
            "id_opportunity": id_opportunity,
            "from_messenger": value,
        }

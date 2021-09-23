from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AccountMoveForm(models.AbstractModel):
    _inherit = 'account.move'

    def traceability_whatsapp(self):
        raise ValidationError("Hola Mundo")
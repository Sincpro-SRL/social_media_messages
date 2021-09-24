from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SincproWhatsapp(models.AbstractModel):
    _name = 'sincpro.whatsapp'
    _description = 'Model to send message by Whatsapp'

    def traceability_whatsapp(self):
         raise ValidationError("Hola Mundo")

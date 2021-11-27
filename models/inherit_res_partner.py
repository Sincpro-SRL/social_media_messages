from odoo import models, fields, api


class AddIdFacebook(models.Model):
    _inherit = 'res.partner'

    id_facebook = fields.Char('ID perfil Facebook', readonly=True)
    from_messenger = fields.Boolean('Obtenido desde messenger', readonly=True, default=False)

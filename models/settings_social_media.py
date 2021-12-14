from odoo import fields, models


class SocialMediaSettings(models.TransientModel):
    _inherit = "res.config.settings"

    test = fields.Many2many('social.media.tokens', string="Facebook tokens")

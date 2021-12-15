from ast import literal_eval

from odoo import fields, models, api


class SocialMediaSettings(models.TransientModel):
    _inherit = "res.config.settings"

    tokens_table = fields.Many2many('social.media.tokens', string="Facebook tokens")

    def get_values(self):
        res = super(SocialMediaSettings, self).get_values()
        values = self.env['ir.config_parameter'].sudo().get_param('social_media_tokens.tokens_table')
        res.update(
            tokens_table=[(6, 0, literal_eval(values))] if values else False, )
        return res

    def set_values(self):
        super(SocialMediaSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('social_media_tokens.tokens_table', self.tokens_table.ids)

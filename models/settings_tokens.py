from odoo import fields, models


class SocialMediaTokens(models.Model):
    _name = "social.media.tokens"

    name_page = fields.Char(string="Nombre de página")
    page_id = fields.Char(string="ID Page Facebook")
    facebook_token = fields.Char(string="Token")


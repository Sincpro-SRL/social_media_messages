from odoo import fields, models


class SocialMediaTokens(models.Model):
    _name = "social.media.tokens"
    _description = "Storages the id and token from facebook page"

    name_page = fields.Char(string="Nombre de página")
    page_id = fields.Char(string="ID Page Facebook")
    facebook_token = fields.Char(string="Token")

    _sql_constraints = [
        (
            'page_id',
            'unique(page_id)',
            'Ya existe este ID de facebook, por favor verifique el ID de la página.\n'
            'Si lo que desea es actualizar, seleccione el token a modificar'
         )
    ]

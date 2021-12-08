from odoo import models, fields


class FacebookPageID(models.Model):
    _name = "facebook.page.id"
    _description = "Storages the id and token from facebook page"

    page_id = fields.Char(string="ID de la página receptora")
    token = fields.Char(string="Token de la página receptora")

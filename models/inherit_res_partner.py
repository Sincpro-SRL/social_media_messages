from odoo import models, fields, api

from .constans import FACEBOOK


class AddIdFacebook(models.Model):
    _inherit = "res.partner"

    id_social_media = fields.Char("ID  de Red Social", readonly=True)
    social_media = fields.Char("Red Social", readonly=True)

    @api.model
    def create_social_media_contact(self, first_name=None, last_name=None, id=None):
        contact = self.search([("id_social_media", "=", id)])
        if not contact["social_media"] == FACEBOOK:
            values = {
                "name": f"{first_name} {last_name}",
                "id_social_media": id,
                "social_media": FACEBOOK,
            }
            return self.create(values)
        return contact

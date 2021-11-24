# -*- coding: utf-8 -*-
from odoo import models, fields, api

FACEBOOK = "Facebook"


class AddIdFacebook(models.Model):
    _inherit = "res.partner"

    id_social_network = fields.Char("ID  de Red Social", readonly=True)
    social_network = fields.Char("Red Social", readonly=True)

    @api.model
    def create_social_network_contact(
        self,
        id=None,
        first_name=None,
        last_name=None,
    ):
        contact = self.search([("id_social_network", "=", id)])
        if not contact["social_network"] == FACEBOOK:
            values = {
                "name": f"{first_name} {last_name}",
                "id_social_network": id,
                "social_network": FACEBOOK,
            }
            return self.create(values)
        return contact

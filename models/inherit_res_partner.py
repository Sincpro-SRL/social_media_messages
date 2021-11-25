# -*- coding: utf-8 -*-
from odoo import models, fields, api

from .constans import FACEBOOK


class AddIdFacebook(models.Model):
    _inherit = "res.partner"

    id_social_network = fields.Char("ID  de Red Social", readonly=True)
    social_network = fields.Char("Red Social", readonly=True)

    @api.model
    def create_social_network_contact(self, user):
        contact = self.search([("id_social_network", "=", user["id"])])
        if not contact["social_network"] == FACEBOOK:
            values = {
                "name": f"{user['first_name']} {user['last_name']}",
                "id_social_network": user["id"],
                "social_network": FACEBOOK,
            }
            return self.create(values)
        return contact

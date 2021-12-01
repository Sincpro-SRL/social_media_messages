from datetime import datetime, timedelta
import logging

from odoo import models, api, fields

from .constants import FACEBOOK

_logger = logging.getLogger(__name__)


class OpportunityManager(models.Model):
    _name = "opportunity.manager"
    _description = "Management the processes to create and verify an opportunity in CRM"

    def opportunity_checker(self, crm_lead, name_opportunity):
        opportunities = crm_lead.search([("name", "=", name_opportunity)])
        for opportunity in opportunities:
            if opportunity["name"] == name_opportunity:
                created_datetime = opportunity["create_date"]
                time_change = created_datetime + timedelta(days=7)
                today = datetime.today()
                if time_change >= today:
                    return opportunity
        return None

    def create_opportunity(self, crm_lead, contact):
        name_opportunity = f"{contact.name}'s opportunity {contact.social_media}"
        opportunity = crm_lead.create(
            {
                "priority": "1",
                "name": name_opportunity,
                "partner_id": contact.id,
                "type": "opportunity",
                "from_messenger_opportunity": True,
            }
        )
        _logger.info(f"New opportunity created: {name_opportunity}")
        return opportunity

    def message_post(self, opportunity, message):
        opportunity.message_post(
            body=f"{message.contact.social_media}: {message.customer_message}"
        )

    def opportunity_validator(self, name_oportunity, contact):
        crm_lead = self.env["crm.lead"]
        opportinity = self.opportunity_checker(crm_lead, name_oportunity)
        if not opportinity:
            opportinity = self.create_opportunity(crm_lead, contact)
        return opportinity

    @api.model
    def opportunity_handler(self, message):
        name_opportunity = (
            f"{message.contact.name}'s opportunity {message.contact.social_media}"
        )
        opportunity = self.opportunity_validator(name_opportunity, message.contact)
        self.message_post(opportunity, message)

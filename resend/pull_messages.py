from odoo import models, api
import logging

from .resend_messages import resend_message
from ..models.constants import NOT_SENT

_logger = logging.getLogger(__name__)


class PullMessages(models.Model):
    _name = 'pull.messages'
    _description = 'Pull de mensajes NOT_SENT'
    _auto = False

    @api.model
    def pull_registers(self):
        token = self.env["ir.config_parameter"].get_param("facebook.facebook_token")
        registers = self.env['social.media.messages']
        registers_not_sent = registers.search([('status_message', '=', NOT_SENT)])

        if registers_not_sent:
            resend_message(registers_not_sent, token)
        else:
            _logger.info("Messages up to date")

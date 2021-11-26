from datetime import datetime

from odoo import models, api
import logging

from .resend_messages import resend_message
from ..models.social_media_messages import ManagementData

_logger = logging.getLogger(__name__)


class PullMessages(models.Model):
    _name = 'pull.messages'
    _description = 'Pull de mensajes NOT_SENT'
    _auto = False

    @api.model
    def pull_registers(self):
        token = self.env["ir.config_parameter"].get_param("facebook.facebook_token")
        registers = self.env['management.data']
        registers_not_sent = registers.search([('status_message', '=', 'NOT_SENT')])
        # values = {
        #     'page_id': 123456789,
        #     'time': 1637878449047,
        #     'message': 'mensaje de prueba',
        #     'social_network': 'FACEBOOK',
        #     'status_message': 'NOT_SENT',
        #     'attempts': 0,
        #     'file_attached': None,
        #     # 'contact': kwargs['contact'].id,
        # }
        # ManagementData.storage_data(self, **values)

        if registers_not_sent:
            resend_message(registers_not_sent, token)
        else:
            _logger.info("Messages up to date")

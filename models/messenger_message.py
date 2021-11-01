from odoo import api, fields, models


class MessengerMessage(models.Model):
    _name = 'messenger.message'

    def send_message_form(self):
        return self.note

    note = fields.Text('Note')


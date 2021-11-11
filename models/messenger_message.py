from odoo import api, fields, models


class MessengerMessage(models.Model):
    _name = 'messenger.message'
    _description = "Implementación vista mensaje a enviar a messenger"
    # _auto = False

    def send_message_form(self):
        data = {
            'crm_id_opportunity': self.env.context['default_res_id'],
            'message': self.note
        }
        self.env['facebook.handler'].handler_send_message(data)

    note = fields.Text('Note')

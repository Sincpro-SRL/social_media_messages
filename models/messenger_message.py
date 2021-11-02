from odoo import api, fields, models


class MessengerMessage(models.Model):
    _name = 'messenger.message'
    _auto = False

    def send_message_form(self):
        data = {
            'crm_id_opportunity': self.env.context['default_res_id'],
            'message': self.note
        }
        self.env['facebook.handler'].handler_send_message(data)

    # @api.model
    # def render_window_message(self):
    #     self.env['facebook.handler'].handler_send_message(self, "Hola")

    note = fields.Text('Note')

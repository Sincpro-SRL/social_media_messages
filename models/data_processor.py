from odoo import models, fields, api
from datetime import date, datetime, timedelta


class CreateContactMessenger(models.Model):
    _name = 'create.contact'
    _description = 'Creacion de contacto desde el Webhook de messenger'
    _auto = False

    @api.model
    def create_partner_webhook_event(self, dic_data):
        res_partner = self.env['res.partner']
        values = {
            'name': f"{dic_data['first_name']} {dic_data['last_name']}",
            'id_facebook': dic_data['id'],
            'from_messenger': True
        }
        return res_partner.create(values)


class DataProcessor(models.Model):
    _name = 'data.processor'
    _description = 'Data processor about message of webhook facebook messenger'
    _auto = False

    @api.model
    def data_checker(self, data):
        user = self.handler_data(data)
        user_res_partner = self.user_checker(user.get('id'))
        if  not user_res_partner:
            user_res_partner = self.env['create.contact'].create_partner_webhook_event(user)
        self.create_opportunity(user_res_partner, user.get('message'))

    def handler_data(self, data):
        user = {
            "first_name": "Brandon",
            "last_name": "Freeman",
            "profile_pic": "https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=4327205417362090&width=1024&ext=1636567735&hash=AeQLwjaETnndOvGzDS0",
            "id": "4327205417362093",
            "message": "mesageee de prueba"
        }
        return user

    def user_checker(self, user_id):
        rest_partner = self.env['res.partner']
        user = rest_partner.search([('id_facebook', '=', user_id)])
        if not user['id_facebook'] == user_id:
            return None
        return user

    def verify_opportunity(self, crm_lead, name_opportunity):
        opportunity = crm_lead.search([('name', '=', name_opportunity)])
        if opportunity['name'] == name_opportunity:
            created_datetime = opportunity['create_date']
            time_change = created_datetime + timedelta(days=7)
            today = datetime.today()
            if time_change >= today:
                return True
        return False

    def create_opportunity(self, user, message):
        crm_lead = self.env['crm.lead']
        name = '{}\'s opportunity Facebook'.format(user['name'])
        if not self.verify_opportunity(crm_lead, name): 
            opportunity = crm_lead.create({
                'priority': '1',
                'name': name,
                'partner_id': user['id'],
                'type': 'opportunity'
            })
            opportunity.message_post(body=message, message_type='comment')

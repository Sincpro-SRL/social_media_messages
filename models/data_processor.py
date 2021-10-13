from odoo import models, fields, api

class CreateContactMessenger(models.Model):
    _name = 'create.contact'
    _description = 'Creacion de contacto desde el Webhook de messenger'
    _auto = False

    @api.model
    def create_partner_webhook_event(self, dic_data):
        values = {
            'name': f"{dic_data['first_name']} {dic_data['last_name']}",
            'id_facebook': dic_data['id'],
            'from_messenger': True
        }
        self.env['res.partner'].create(values)


class DataProcessor(models.Model):
    _name = 'data.processor'
    _description = 'Data processor about message of webhook facebook messenger'
    _auto = False

    @api.model
    def data_checker(self, data):
        user = self.handler_data(data)
        print(user)
        if  not self.user_checker(user.get('id')):
            self.create_user(user)
        self.create_opportunity(user)

    def handler_data(self, data):
        user = {
            "first_name": "Jairo",
            "last_name": "Sandoval Velasquez",
            "profile_pic": "https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=4327205417362090&width=1024&ext=1636567735&hash=AeQLwjaETnndOvGzDS0",
            "id": "4327205417362090",
            "message": "mesageee de prueba"
        }
        return user

    def user_checker(self, user_id):
        users = self.env['res.partner'].search([])
        for user in users:
            if user.id_facebook == user_id:
                return True
        return False

    def create_user(self, user):
        self.env['create.contact'].create_partner_webhook_event(user)

    def create_opportunity(self, user):
        crm_lead = self.env['crm.lead']
        crm_lead.create({
        'priority': '0',
        'name': user.get('last_name'),
        })
    

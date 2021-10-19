import requests
from odoo import fields, models, api

class FacebookHadler(models.Model):
    _name = 'facebook handler'
    _description = 'manejar datos de un perfil de facebook'
    _auto = False

    @api.model
    def get_info_profile(self, user):
        token = self.env['ir.config_parameter'].sudo().get_param("facebook.facebook_token")

        user_id = user["sender"]["id"]
        if not token and not user_id:
            raise Exception("Token y usuario invalidos")
        
        profile = requests.get(f'{FACEBOOK_API}/{user_id}?access_token={token}')
        
        facebook_response = profile.json()
        return facebook_response
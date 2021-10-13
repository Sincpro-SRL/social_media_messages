from odoo import fields, models, api

class WhatsappConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    whatsapp_crm= fields.Boolean("")
    whatsapp_sales = fields.Boolean("")
    whatsapp_inventory = fields.Boolean("")
    whatsapp_token = fields.Char(string="token")
    facebook_crm= fields.Boolean("")
    facebook_sales = fields.Boolean("")
    facebook_inventory = fields.Boolean("")
    facebook_token = fields.Char(string="token")

    def set_values(self):
        res = super(WhatsappConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('whatsapp.whatsapp_crm', self.whatsapp_crm)
        self.env['ir.config_parameter'].set_param('whatsapp.whatsapp_sales', self.whatsapp_sales)
        self.env['ir.config_parameter'].set_param('whatsapp.whatsapp_inventory', self.whatsapp_inventory)
        self.env['ir.config_parameter'].set_param('whatsapp.whatsapp_token', self.whatsapp_token)
        
        self.env['ir.config_parameter'].set_param('facebook.facebook_crm', self.facebook_crm)
        self.env['ir.config_parameter'].set_param('facebook.facebook_sales', self.facebook_sales)
        self.env['ir.config_parameter'].set_param('facebook.facebook_inventory', self.facebook_inventory)
        self.env['ir.config_parameter'].sudo().set_param('facebook.facebook_token', self.facebook_token)
        return res

    def get_values(self):
        res = super(WhatsappConfigSettings, self).get_values()
        whatsapp_crm = self.env['ir.config_parameter'].get_param("whatsapp.whatsapp_crm")
        whatsapp_sales = self.env['ir.config_parameter'].get_param("whatsapp.whatsapp_sales")
        whatsapp_inventory = self.env['ir.config_parameter'].get_param("whatsapp.whatsapp_inventory")
        whatsapp_token = self.env['ir.config_parameter'].get_param("whatsapp.whatsapp_token")

        facebook_crm = self.env['ir.config_parameter'].get_param("facebook.facebook_crm")
        facebook_sales = self.env['ir.config_parameter'].get_param("facebook.facebook_sales")
        facebook_inventory = self.env['ir.config_parameter'].get_param("facebook.facebook_inventory")
        facebook_token = self.env['ir.config_parameter'].sudo().get_param("facebook.facebook_token")
        
        
        res.update({
            'facebook_crm': facebook_crm,
            'facebook_sales': facebook_sales,
            'facebook_inventory': facebook_inventory,
            'facebook_token': facebook_token,
        })
        return res


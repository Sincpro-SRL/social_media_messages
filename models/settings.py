from odoo import fields, models, api

class WhatsappConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    whatsapp_crm= fields.Boolean("")
    whatsapp_sales = fields.Boolean("")
    whatsapp_inventory = fields.Boolean("")

    def set_values(self):
        res = super(WhatsappConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('whatsapp.whatsapp_crm', self.whatsapp_crm)
        self.env['ir.config_parameter'].set_param('whatsapp.whatsapp_sales', self.whatsapp_sales)
        self.env['ir.config_parameter'].set_param('whatsapp.whatsapp_inventory', self.whatsapp_inventory)
        return res

    def get_values(self):
        res = super(WhatsappConfigSettings, self).get_values()
        whatsapp_crm = self.env['ir.config_parameter'].get_param("whatsapp.whatsapp_crm")
        whatsapp_sales = self.env['ir.config_parameter'].get_param("whatsapp.whatsapp_sales")
        whatsapp_inventory = self.env['ir.config_parameter'].get_param("whatsapp.whatsapp_inventory")
        res.update({
            'whatsapp_crm': whatsapp_crm,
            'whatsapp_sales': whatsapp_sales,
            'whatsapp_inventory': whatsapp_inventory
        })
        return res

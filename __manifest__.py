{
    'name': 'Sincpro Whatsapp',
    'description': '',
    'depends': [
        'base',
        'account',
        'sale',
        'crm',
    ],
    'data': [
        'views/settings.xml',
        'security/ir.model.access.csv',
        'views/view_move_form_whatsapp_button.xml',
        'views/view_order_form_whatsapp_button.xml',
        'views/view_crm_lead_form_whatsapp_button.xml',
    ],
}
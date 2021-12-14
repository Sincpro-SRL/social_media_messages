{
    "name": "Sincpro RRSS Messages",
    "description": "",
    "depends": [
        "base",
        "account",
        "sale",
        "crm",
        "mail",
    ],
    "data": [
        "views/templates.xml",
        "views/view_messenger_message.xml",
        "views/settings_social_media.xml",
        "views/settings_tokens.xml",
        "security/ir.model.access.csv",
        "views/view_contact_facebook_profile.xml",
        "resend/cron_resend_messages.xml",
    ],
    "qweb": [
        "static/src/xml/chatter_messenger.xml",
    ],
    "application": True,
}

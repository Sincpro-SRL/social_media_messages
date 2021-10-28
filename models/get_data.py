from odoo import models, api


class GetDataClass(models.AbstractModel):
    _name = 'get.data'

    @api.model
    def render_html(self, docids, data=None):
        docargs = {
           'doc_ids': self.ids,
           'doc_model': self.model,
           'data': data,
        }
        return self.env['report'].render('module_name.report_name', docargs)
from odoo import api, SUPERUSER_ID

def enable_delivery_methods(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.config_parameter'].sudo().set_param('delivery.use_delivery_methods', 'True')

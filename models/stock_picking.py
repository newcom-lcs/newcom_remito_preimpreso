# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
# from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES
from odoo.exceptions import UserError, ValidationError
# from odoo.osv import expression
# from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, format_datetime, format_date, groupby
# from odoo.tools.float_utils import float_compare, float_is_zero, float_round


class Picking(models.Model):
    _name = "stock.picking"
    _inherit = "stock.picking"

    def _sanity_check(self, separate_pickings=True):
        """ Sanity check for `button_validate()`
            :param separate_pickings: Indicates if pickings should be checked independently for lot/serial numbers or not.
        """

        maximo = 25
        
        if len(self.move_line_ids_without_package) > maximo:
            excedente = len(self.move_line_ids_without_package) - maximo
            raise UserError(_('Sólo se pueden despachar hasta ' + str(maximo) + ' items por remito, por favor elimine ' + str(excedente) + ' items y vuelva a intentarlo'))

        
        super()._sanity_check(separate_pickings)



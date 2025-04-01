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

        max_prod_con_serie = 90
        max_prod_sin_serie = 30
        # Verificar si el picking es de despacho
        if self.picking_type_code == 'outgoing':
            # Contar la cantidad de productos con y sin serie
            productos_con_serie = 0
            productos_sin_serie = 0
            for move_line in self.move_line_ids_without_package:
                if move_line.qty_done > 0:
                    if move_line.product_id.tracking == 'serial':
                        productos_con_serie += 1
                    else:
                        productos_sin_serie += 1

            # Ajustar el límite según la cantidad de productos con y sin serie
            if productos_con_serie > 0 and productos_sin_serie > 0:
                # Si hay productos con y sin serie, aplicar la relación 3:1
                limite = int((productos_con_serie * 3) + productos_sin_serie)
                maximo = max_prod_con_serie
                if limite > maximo:
                    excedente = limite - maximo
                    raise UserError(_('Sólo se pueden despachar hasta ' + str(maximo) + ' items por remito, por favor elimine ' + str(excedente) + ' items y vuelva a intentarlo'))
            elif productos_con_serie > 0:
                # Si todos los productos tienen serie, el límite es 90
                if productos_con_serie > max_prod_con_serie:
                    excedente = productos_con_serie - max_prod_con_serie
                    raise UserError(_('Sólo se pueden despachar hasta ' + str(max_prod_con_serie) + ' items por remito, por favor elimine ' + str(excedente) + ' items y vuelva a intentarlo'))
            else:
                # Si no hay productos con serie, el límite es 30
                if productos_sin_serie > max_prod_sin_serie:
                    excedente = productos_sin_serie - max_prod_sin_serie
                    raise UserError(_('Sólo se pueden despachar hasta ' + str(max_prod_sin_serie) + ' items por remito, por favor elimine ' + str(excedente) + ' items y vuelva a intentarlo'))

        
        super()._sanity_check(separate_pickings)

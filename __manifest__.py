# -*- coding: utf-8 -*-
{
    'name': 'Remito Preimpreso',
    'license': 'LGPL-3',
    'version': '16.0.1',
    'category': 'Stock',
    'depends': [
        'stock',
        'l10n_ar',
        'l10n_ar_stock',
        'l10n_ar_stock_delivery',
        'delivery',
        ],
    'data':[
       #'reports/remito_preimpreso_report.xml',
       'reports/remito_preimpreso_report_template.xml',
    ],
    'auto_install': False,
    'installable' : True,
    'application' : False,
}
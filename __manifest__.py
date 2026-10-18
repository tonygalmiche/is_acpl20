# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 20 pour ACPL',
    'version'  : '20.0.0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 20 pour ACPL
===================================================
Reprise d'is_acpl14 (Odoo 14).
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'stock',
        'sale_management',
        'account',
],
    'data' : [
        'security/ir.access.csv',

        # Migration v20 : vues, menus et rapports désactivés pour installer d'abord les modèles
        # 'report/layouts.xml',
        # 'report/conditions_generales_de_vente_templates.xml',
        # 'report/sale_report_templates.xml',
        # 'views/report_invoice.xml',
        # 'views/account_move_view.xml',
        # 'views/sale_view.xml',
        # 'views/partner_view.xml',
        # 'views/is_export_compta_view.xml',
        # 'views/product_view.xml',
        # 'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}


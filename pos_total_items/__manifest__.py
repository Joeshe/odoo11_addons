# -*- coding: utf-8 -*-
{
    'name': 'POS Total Items in Cart',
    'version': '1.0',
    'price' : '4.99',
    'currency': 'USD',
    'summary': 'POS Total Items in Cart',
    'description': """
POS Total Items in Cart
=======================

This module displays the total items(# of pos orderlines) in pos cart and pos receipt.


Keywords: Odoo POS Total Cart Items
""",
    'category': 'Point of Sale',
    'author': 'SFSolutions',
    'website': 'https://apps.odoo.com/apps/modules/browse?author=SFSolutions',
    'depends': ['point_of_sale'],
    'data': ['views/pos_templates.xml'],
    'demo': [],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
    'application': False,
    'auto_install': False,
    #'images': ['static/description/pos_total_items.png'],
}
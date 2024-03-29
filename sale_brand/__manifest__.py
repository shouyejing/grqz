# pylint: disable=manifest-required-author
# Copyright 2017 Humanytek.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Sale Order - Brand",
    'summary': """
    """,
    'author': "Humanytek",
    'website': "http://www.humanytek.com",
    'license': 'AGPL-3',
    'category': 'Sale',
    'version': '11.0.1.0.0',
    'depends': ['sale', 'product_brand', 'account'],
    'data': [
        'view/sale_view.xml',
        'view/account_invoice_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
}

# -*- coding: utf-8 -*-
{
    'name': "Booking Order 10",

    'summary': """
        Booking Order for Odoo 10""",

    'description': """
        Booking Order for Odoo 10
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Sales',
    'version': '1,0',
    'installable': True,
    'application': True,

    'depends': ['base', 'sale'],

    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_state.xml',
        'views/work_order_views.xml',
        'views/booking_order_views.xml',
        'views/service_team_views.xml',
        'views/menu.xml',
        'report/report_work_order.xml',
        'report/report.xml',
        'data/data.xml'
    ],
}
{
    'name': "Booking Order",
    'summary': "Booking Order for Odoo 14",
    'description': "Booking Order for Odoo 14",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Sales',
    'version': '1.0',
    'application': True,

    'depends': [
        'base', 
        'mail', 
        'sale', 
        'sales_team'
    ],

    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_state.xml',
        'data/data.xml',
        'views/menu.xml',
        'views/booking_order_views.xml',
        'views/work_order_views.xml',
        'views/service_team_views.xml',
        'report/report.xml',
        'report/work_order_report.xml',
    ],

}

# -*- coding: utf-8 -*-

{
    "name": "Invoice Payment Latitude And Longitude",
    "version": "17.0.0.1",
    "category": "Invoices & Payments",
    "license": "LGPL-3",
    "description": "This module set current location latitude and longitude when payment was confirm.",
    "summary": 'This module set current location latitude and longitude in account payment when invoice payment confirm.',
    "author": " Mr. Tanmay Kathiriya - Odoo Developer",
    "website": " ",
    "depends": ['base', 'account'],
    "data": [
        "views/account_move_view.xml",
        "views/account_payment_view.xml",
    ],
    "installable": True,
}

# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    latitude = fields.Char(string="Latitude", readonly=True, copy=False)
    longitude = fields.Char(string="Longitude", readonly=True, copy=False)

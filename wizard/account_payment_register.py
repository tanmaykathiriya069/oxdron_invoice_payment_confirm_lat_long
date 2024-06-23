# -*- coding: utf-8 -*-

import geocoder

from odoo import fields, models


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    def get_current_lat_long(self):
        location_data = geocoder.ip('me')
        if location_data.latlng:
            latitude, longitude = location_data.latlng
            return latitude, longitude
        return None, None

    def _create_payments(self):
        payments = super(AccountPaymentRegister, self)._create_payments()
        for payment in payments.reconciled_invoice_ids:
            if payments.id not in payment.invoice_payment_ids.ids:
                # Add the payment ID to invoice_payment_ids
                payment.write({
                    'invoice_payment_ids': [(4, payments.id)]
                })
            latitude, longitude = self.get_current_lat_long()
            # Update 'latitude' and 'longitude' fields with the obtained values
            if latitude is not None and longitude is not None and payment and payments:
                payments.write({'latitude': str(latitude), 'longitude': str(longitude)})
        return payments
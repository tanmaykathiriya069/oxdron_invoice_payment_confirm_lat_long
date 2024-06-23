# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_payment_ids = fields.Many2many('account.payment',
                                           'invoice_payment_ids'
                                           'invoice_id', 'payment_id',
                                           readonly=True,
                                           copy=False)

    def action_show_payment(self):
        self.ensure_one()
        if self.invoice_payment_ids:
            self.ensure_one()
            return {
                    'type': 'ir.actions.act_window',
                    'name': 'Account Payment',
                    'res_model': 'account.payment',
                    'domain': [('id', '=', self.invoice_payment_ids.ids)],
                    'view_mode': 'tree,form',
                    'target': 'current'
                }

    def button_draft(self):
        res = super().button_draft()
        if self.invoice_payment_ids:
            self.invoice_payment_ids.unlink()
        return res
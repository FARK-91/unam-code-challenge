# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UnamIntervalTime(models.Model):
    _name = 'unam.interval.time'
    _description = 'UNAM Interval Times'
    _rec_name = 'name'

    name = fields.Char(string="Name", readonly=True)
    interval_number = fields.Integer(string="Interval Number", required=True, default=1)
    interval_type = fields.Selection(
        string="Interval Type",
        selection=[('hours', 'Hours'), ('days', 'Days'), ('weeks', 'Weeks'), ('months', 'Months'), ('years', 'Years')],
        store=True,
        readonly=False,
        required=True,
        default='months'
    )

    @api.onchange('interval_number', 'interval_type')
    def _onchange_custom_name(self):
        for rec in self:
            rec.name = f'{rec.interval_number} {rec.interval_type}'
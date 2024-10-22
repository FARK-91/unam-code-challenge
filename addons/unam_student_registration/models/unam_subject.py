# -*- coding: utf-8 -*-

from odoo import models, fields

class UnamSubject(models.Model):
    _name = 'unam.subject'
    _description = 'UNAM Subject'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    credit_limit = fields.Integer(string="Max Credits")
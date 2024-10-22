# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
from datetime import date

_logger = logging.getLogger(__name__)

class UnamStudent(models.Model):
    _name = 'unam.student'
    _description = 'UNAM Students inherited from res.partner'
    _inherits = {'res.partner': 'partner_id'}
    _rec_name = 'name'

    partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', auto_join=True, index=True, string='Related Partner')
    birth_date = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age")

    @api.onchange('birth_date')
    def _onchage_student_age(self):
        '''
        Calculate a student's age from their date of birth.
        onchange Args:
            birth_date: A text string in 'YYYY-MM-DD' format.
        
        Record Set:
            An integer representing age.
        '''
        for record in self:
            # _logger.warning("******* _onchange_student_age ********")
            today = date.today()
            record.age = today.year - record.birth_date.year - ((today.month, today.day) < (record.birth_date.month, record.birth_date.day)) if record.birth_date else 0
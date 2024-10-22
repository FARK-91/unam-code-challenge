# -*- coding: utf-8 -*-

from odoo import models, fields

class UnamRegistration(models.Model):
    _name = 'unam.registration'
    _description = 'UNAM Registration'
    _rec_name = 'student_id'

    student_id = fields.Many2one('unam.student', required=True, ondelete='restrict', string='Student')
    course_ids = fields.Many2many('unam.course', 'unam_registration_course_rel',
        'registration_id', 'course_id', string='Courses')
    registration_date = fields.Date(string="Registration date", required=True)
    state = fields.Selection(
        selection=[
            ('pending', 'pending'),
            ('done', 'confirmed'),
            ('cancel', 'Cancelled'),
        ],
        string='Status',
        required=True,
        default='pending',
    )

    def button_cancel(self):
        self.state = 'cancel'

    def button_confirm(self):
        self.state = 'done'

    def button_restart(self):
        self.state = 'pending'
    
# -*- coding: utf-8 -*-

from odoo import models, fields

class UnamTeacher(models.Model):
    _name = 'unam.teacher'
    _description = 'UNAM Teacher inherited from res.partner'
    _inherits = {'res.partner': 'partner_id'}
    _rec_name = 'name'

    partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', auto_join=True, index=True, string='Related Partner')
    subject_ids = fields.One2many('unam.teacher.subject', 'teacher_id', ondelete='cascade', string='Subject')

class UnamTeacherSubject(models.Model):
    _name = 'unam.teacher.subject'
    _description = 'UNAM Teacher Subject Relation'

    subject_id = fields.Many2one('unam.subject', required=True, ondelete='restrict', string='Subject')
    teacher_id = fields.Many2one('unam.teacher', ondelete='restrict', string='Teacher', invisible=True)
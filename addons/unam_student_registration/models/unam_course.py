# -*- coding: utf-8 -*-

from odoo import models, fields

class UnamCourse(models.Model):
    _name = 'unam.course'
    _description = 'UNAM Courses inherited from product.template'
    _inherits = {'product.template': 'product_tmpl_id'}
    _rec_name = 'name'

    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        # Automatic field value Set: type -> 'consumible'
        defaults.setdefault('type', 'consu')

        return defaults

    product_tmpl_id = fields.Many2one('product.template', required=True, ondelete='restrict', auto_join=True, index=True, string='Related Product')
    interval_id = fields.Many2one('unam.interval.time', required=True, ondelete='restrict', string='Duration')
    teacher_subject_ids = fields.One2many('unam.course.teacher.subject', 'course_id', ondelete='cascade', string='Subjects')
    start_date = fields.Date(string="Start date")
    student_limit = fields.Integer(string="Max Students")

class UnamCourseTeacherSubject(models.Model):
    _name = 'unam.course.teacher.subject'
    _description = 'UNAM Course Teacher Subject Relation'

    subject_id = fields.Many2one('unam.subject', required=True, ondelete='restrict', string='Subject')
    teacher_id = fields.Many2one('unam.teacher', required=True, ondelete='restrict', string='Teacher')
    course_id = fields.Many2one('unam.course', ondelete='restrict', string='Course')
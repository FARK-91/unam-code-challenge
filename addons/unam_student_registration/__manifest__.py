# -*- coding: utf-8 -*-
{
    'name': "UNAM - Inscripción Alumnos",

    'summary': "Módulo de gestión para inscripciones de alumnnos",

    'description': """
      * Nuevo modelo para registro de alumnos.
      * Nuevo modelo para registro de cursos.
      * Nuevo modelo para registro de profesores.
      * Nuevo modelo para registro de inscripciones.
      * Nuevo modelo para registro de materias.
    """,
    'author': "UNAM",
    'website': "https://www.unam.mx/",
    'category': 'Customizations',
    'version': '17.0.1.0.0',
    'depends': ['base_setup', 
                'mail',
                'stock',
                'contacts'],
    'data': [
        'data/unam_interval_time.xml',
        'data/unam_subject.xml',
        'security/student_registration_groups.xml',
        'security/ir.model.access.csv',
        'views/unam_student.xml',
        'views/unam_interval_time.xml',
        'views/unam_course.xml',
        'views/unam_teacher.xml',
        'views/unam_subject.xml',
        'views/unam_registration.xml',
    ]
}


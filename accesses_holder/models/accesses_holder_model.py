# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccessesStorage(models.Model):
    _name = 'accesses.storage'
    _description = 'accesses_storage'
    name = fields.Char('Name')
    project_id = fields.Many2one('project.project', string='project')
    data = fields.Html(string='accesses data')

    user_ids = fields.Many2many(
        'res.users',
        string=u"users")

    color = fields.Integer('Color index')
    kanban_state = fields.Selection([('normal', 'In Progress'), ('blocked', 'blocked'), ('done', 'Done')], 'Kanban State', default='normal')



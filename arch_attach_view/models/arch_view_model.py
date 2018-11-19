# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Project(models.Model):
    _name = "project.project"
    _inherit = "project.project"


    def _compute_attached_docs_count(self):
        Attachment = self.env['ir.attachment']
        for project in self:
            task_ids = self.env['project.task'].search(
                [('project_id', '=', project.id), '|', ('active', '=', True), ('active', '=', False)])
            project.doc_count = Attachment.search_count([
                '|',
                '&',
                ('res_model', '=', 'project.project'), ('res_id', '=', project.id),
                '&',
                ('res_model', '=', 'project.task'), ('res_id', 'in', task_ids.ids)
            ])

    @api.multi
    def attachment_tree_view(self):
        self.ensure_one()
        task_ids = self.env['project.task'].search([('project_id','=', self.id),'|',('active','=',True),('active','=',False)])
        domain = [
            '|',
            '&', ('res_model', '=', 'project.project'), ('res_id', 'in', self.ids),
            '&', ('res_model', '=', 'project.task'), ('res_id', 'in', task_ids.ids)]
        return {
            'name': _('Attachments'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                           Documents are attached to the tasks and issues of your project.</p><p>
                           Send messages or log internal notes with attachments to link
                           documents to your project.
                       </p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }
# -*- coding: utf-8 -*-
# © 2017 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class project_task_type_class(models.Model):
    _inherit = 'project.task.type'

    calculated_item = fields.Boolean("Calculable level",default=False)
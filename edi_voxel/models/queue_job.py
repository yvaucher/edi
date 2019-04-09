# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, models


class QueueJob(models.Model):
    _inherit = 'queue.job'

    @api.multi
    def voxel_do_now(self):
        self.sudo().write({'eta': 0})

    @api.multi
    def voxel_cancel_now(self):
        self.sudo().filtered(
            lambda x: x.state in ['pending', 'enqueued']
        ).unlink()

    @api.multi
    def voxel_requeue_sudo(self):
        self.sudo().requeue()

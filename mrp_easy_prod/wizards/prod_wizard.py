# Copyright 2019  - jeo Software
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import api, models, fields


class WizardModel(models.TransientModel):
    _name = "mrp.wizard"

    name = fields.Char(

    )
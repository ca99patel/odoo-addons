# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    allow_website_menu_multilevel = fields.Boolean(string="Allow Multilevel Menu")
    website_menu_levels = fields.Integer(string="Menu Levels", default=2)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res.update(
            allow_website_menu_multilevel = get_param('website_menu_multilevel.allow_website_menu_multilevel'),
            website_menu_levels = int(get_param('website_menu_multilevel.website_menu_levels'))
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].set_param
        set_param('website_menu_multilevel.allow_website_menu_multilevel', self.allow_website_menu_multilevel)
        set_param('website_menu_multilevel.website_menu_levels', self.website_menu_levels)

odoo.define('website_menu_multilevel.multilevel_menu', function (require) {
    'use strict';

var EditMenuDialog = require('website.contentMenu').EditMenuDialog;

EditMenuDialog.include({

        start: function () {
            var r = this._super.apply(this, arguments);
            this.$('.oe_menu_editor').nestedSortable({
                listType: 'ul',
                handle: 'div',
                items: 'li',
                maxLevels: menu_levels,
                toleranceElement: '> div',
                forcePlaceholderSize: true,
                opacity: 0.6,
                placeholder: 'oe_menu_placeholder',
                tolerance: 'pointer',
                attribute: 'data-menu-id',
                expression: '()(.+)', // nestedSortable takes the second match of an expression (*sigh*)
            });
            return r;
        }
    });
});
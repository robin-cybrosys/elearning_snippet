// /** @odoo-module **/
odoo.define('elearning_snippet.dynamic', function (require) {
    var PublicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var Dynamic = PublicWidget.Widget.extend({
        selector: '.elearning_snippet',
        start: function () {
            var self = this;
            rpc.query({
                route: '/total_product_sold',
                params: {},
            }).then(function (result) {
                self.$('#total_sold').text(result);
            });
        },
    });
    PublicWidget.registry.elearning_snippet = Dynamic;
    return Dynamic;
 });
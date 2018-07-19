odoo.define('pos_total_items.pos_total_items', function (require) {
"use strict";
var screens = require('point_of_sale.screens');
var core = require('web.core');
var QWeb = core.qweb;
var pos_model = require('point_of_sale.models');

screens.OrderWidget.include({
    update_summary: function(){
        this._super();
        var order = this.pos.get_order();
        if (!order.get_orderlines().length) {
            return;
        }
        var items = order? order.orderlines.length : 0;
        this.el.querySelector('.summary .total .subentry1 .value').textContent = items;
    },
});

var _super_order = pos_model.Order.prototype;

 pos_model.Order = pos_model.Order.extend({
        get_total_items: function(){
            return this.orderlines.length;
        },
    });

});
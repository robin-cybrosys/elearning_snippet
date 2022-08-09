from odoo import http
from odoo.http import request


class Sales(http.Controller):
    @http.route(['/total_product_sold'], type="json", auth="public")
    def sold_total(self):
        sale_obj = request.env['sale.order'].sudo().search([
            ('state', 'in', ['done', 'sale']),
        ])
        total_sold = sum(sale_obj.mapped('order_line.product_uom_qty'))
        return total_sold

# -*- coding: utf-8 -*-
# from odoo import http


# class ElearningSnippet(http.Controller):
#     @http.route('/elearning_snippet/elearning_snippet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/elearning_snippet/elearning_snippet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('elearning_snippet.listing', {
#             'root': '/elearning_snippet/elearning_snippet',
#             'objects': http.request.env['elearning_snippet.elearning_snippet'].search([]),
#         })

#     @http.route('/elearning_snippet/elearning_snippet/objects/<model("elearning_snippet.elearning_snippet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('elearning_snippet.object', {
#             'object': obj
#         })

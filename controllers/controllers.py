# -*- coding: utf-8 -*-
# from odoo import http


# class Quintoarte(http.Controller):
#     @http.route('/quintoarte/quintoarte/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quintoarte/quintoarte/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quintoarte.listing', {
#             'root': '/quintoarte/quintoarte',
#             'objects': http.request.env['quintoarte.quintoarte'].search([]),
#         })

#     @http.route('/quintoarte/quintoarte/objects/<model("quintoarte.quintoarte"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quintoarte.object', {
#             'object': obj
#         })

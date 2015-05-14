# -*- coding: utf-8 -*-
from openerp import http

# class OdooTwitterTracker(http.Controller):
#     @http.route('/odoo_twitter_tracker/odoo_twitter_tracker/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_twitter_tracker/odoo_twitter_tracker/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_twitter_tracker.listing', {
#             'root': '/odoo_twitter_tracker/odoo_twitter_tracker',
#             'objects': http.request.env['odoo_twitter_tracker.odoo_twitter_tracker'].search([]),
#         })

#     @http.route('/odoo_twitter_tracker/odoo_twitter_tracker/objects/<model("odoo_twitter_tracker.odoo_twitter_tracker"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_twitter_tracker.object', {
#             'object': obj
#         })
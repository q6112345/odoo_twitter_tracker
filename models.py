# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Tweeter(models.Model):
    _name = "ott.tweeter"
    name = fields.Char(string="Screen Name", request=True)
    description = fields.Text()

class Tweet(models.Model):
    _name = "ott.tweet"
    content = fields.Char()
    poster = fields.Many2one('ott.tweeter', ondelete="cascade", string="Poster")

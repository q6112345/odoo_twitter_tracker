# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Tweeter(models.Model):
    _name = "ott.tweeter"
    name = fields.Char(string="Screen Name", request=True)
    description = fields.Text()
    tweets_ids = fields.One2many('ott.tweet', 'poster_id', string="Tweets")

class Tweet(models.Model):
    _name = "ott.tweet"
    content = fields.Char(string="Content")
#    time =fields.Char(string="Time")
    poster_id = fields.Many2one('ott.tweeter', ondelete="cascade", string="Poster")

# -*- coding: utf-8 -*-

from openerp import models, fields, api
from urllib2 import urlopen
from lxml import etree

ENDPOINT = "https://twitter.com/"

class Tweeter(models.Model):
    _name = "ott.tweeter"
    name = fields.Char(string="Screen Name", request=True)
    description = fields.Text()
    tweets_ids = fields.One2many('ott.tweet', 'poster_id', string="Tweets")

    @api.one
    def get_tweet(self):
        for record in self:
            poster_id = record.name
            url = ENDPOINT + record.name
            html = urlopen(url).read()
            dom = etree.fromstring(html)
            tweet_list = dom.xpath('//div[@class="ProfileTweet-contents"]')
            for tweet in tweet_list:
                content =tweet
                self.pool.get('ott.tweet').add_tweet(poster_id, content)
                #record.tweets_id.content = tweet
                #self.env.cr.execute("some_sql", param1, param2, param3)


class Tweet(models.Model):
    _name = "ott.tweet"
    content = fields.Char(string="Content")
#    time =fields.Char(string="Time")
    poster_id = fields.Many2one('ott.tweeter', ondelete="cascade", string="Poster")

    def add_tweet(self, poster_id, content):
        self.creat({'poster_id':poster_id, 'content':content})
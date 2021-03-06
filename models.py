# -*- coding: utf-8 -*-

from openerp import models, fields, api
import oauth2 as oauth
import json
import logging
_logger = logging.getLogger(__name__)

CONSUMER_KEY = 'UvbYbzVrAnkQyEmFdnulJCqmF'
CONSUMER_SECRET = 'jqQyxcaWm2RjKzqJVC9VbsTTOyydY2luOP7icCvb9kGS9Pz1eH'
KEY = '350263395-1AQhVGKaUpfy6XkGz7nRHr5B9PZcV01x4Xwxn88p'
SECRET = 'wm5TFVKhSTRD1mN72fGgT2TNA5KhfqkfmOGLEreBo0O7D'

class TwitterClient(object):
    def oauth_req(self, url, http_method = 'GET', post_body = '', http_headers = ''):
        consumer = oauth.Consumer(key = CONSUMER_KEY, secret = CONSUMER_SECRET)
        token = oauth.Token(key = KEY, secret = SECRET)
        client = oauth.Client(consumer, token)
        resp, content = client.request(url,
            method = http_method,
            body = post_body,
            headers = http_headers
        )
        jdata = json.loads(content)
        return jdata

    def get(self, url):
        jdata = self.oauth_req(url)
        return jdata


class TwitterAccount(models.Model):
    _name = "ott.twitter_account"
    name = fields.Char(string="Screen Name", request=True)
    description = fields.Text()
    tweets_ids = fields.One2many('ott.tweet', 'poster_id', string="Tweets")

    @api.model
    def get_tweet(self):
        tweets = self.env['ott.tweet']
        t = TwitterClient()
        twitter_accounts = self.env['ott.twitter_account'].search([])
        for twitter_account in twitter_accounts:
            screen_name = twitter_account.name
            url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?count=20&screen_name=%s' % screen_name
            response = t.get(url)
            for tweet_dict in response:
                tweet_id = tweet_dict['id']
                tweet_content = tweet_dict['text']
                tweet_lid = self.env['ott.tweet'].search([('tweet_id', '=', tweet_id)])
                if not tweet_lid:
                    tweets.create({
                              'content': tweet_content,
                              'tweet_id': tweet_id,
                              "poster_id": twitter_account.id,
                            })




class Tweet(models.Model):
    _name = "ott.tweet"
    content = fields.Char(string="Content")
    tweet_id = fields.Float(sting="Tweet ID", digits=(0,0))
    poster_id = fields.Many2one('ott.twitter_account', ondelete="cascade", string="Poster")
    #poster_id i an interger
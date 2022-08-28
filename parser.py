# -*- coding: utf-8 -*-
"""
Parsering of sites
"""
import requests


__author__ = 'Vadim Arsenev'
__version__ = '0.9.3'
__data__ = '28.08.2022'


class Parser(object):

    def __init__(self, url, headers='', cookies='', params=''):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/67.0.3396.79 Safari/537.36',
        }
        self.headers.update(headers)
        self.cookies = cookies
        self.params = params

    def get_response(self):
        """Connection to the site"""
        self.response = requests.get(self.url, headers=self.headers, \
            cookies=self.cookies, params=self.params)
        if self.response.status_code != 200:
            print('Update a cookies in the settings')
        self.response.encoding = 'utf-8'

    def get_json(self):
        """Getting json data"""
        try:
            self.data = self.response.json()
        except AttributeError as e:
            print(e)
            self.data = ''
    
    def get_html(self):
        """Getting html"""
        self.data = self.response.text

    def parser_result(self):
        self.get_response()
        self.get_json()
        return self.data


    def parser_resultHtml(self):
        self.get_response()
        self.get_html()
        return self.data


class ParserPost(Parser):

    def __init__(self, addUrl, payload):
        self.addUrl = addUrl
        self.payload = payload

    def get_response(self):
        """Connection to the site. Sending Post request"""
        self.response = requests.post(self.addUrl, data=self.payload)
        self.response.encoding = 'utf-8'

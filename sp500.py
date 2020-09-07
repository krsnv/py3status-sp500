# -*- coding: utf-8 -*-
"""SPX (SP500) Current Price with changes indicator"""

import requests

from lxml import html


class Py3status:

    def __init__(self):
        self.full_text = 'SP500'

    def sp500(self):
        xpath = '/html/body/main/div/div/div[3]/div/div[1]/div[2]/div/table/tbody/tr[1]/th[1]/div/div/div/span//text()'
        xpath_change = '/html/body/main/div/div/div[3]/div/div[1]/div[2]/div/table/tbody/tr[1]/th[2]/div/div/span//text()'
        xpatp_percents = '/html/body/main/div/div/div[3]/div/div[1]/div[2]/div/table/tbody/tr[1]/th[3]/div/div/span//text()'
        cont  = requests.get("https://markets.businessinsider.com/index/realtime-chart/s&p_500").content
        tree  = html.fromstring(cont)
        price = tree.xpath(xpath)
        change = tree.xpath(xpath_change)
        change_percents = tree.xpath(xpatp_percents)

        return {
            'full_text': f"SPX: {price[0]} ({change[0]} {change_percents[0]})",
            'cached_until': 60
        }


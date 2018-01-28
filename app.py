# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 00:59:12 2018

@author: Daiwi
"""

import config
import telebot
import urllib.request
import json


bot = telebot.TeleBot(config.token)


def calcEthCount():
    request = urllib.request.Request("https://api.ethermine.org/miner/0x6e605111a81cAe553871a48c4a14a872cA27e6D8/currentStats", headers=config.hdr)
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need
    json_A = json.loads(data.decode("utf-8"))
    return float(json_A['data']['unpaid']/1000000000000000000)


def calcEthRub():
    request = urllib.request.Request("https://api.coinmarketcap.com/v1/ticker/Ethereum/?convert=RUB", headers=config.hdr)
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need
    json_A = json.loads(data.decode("utf-8"))
    return float(json_A[0]['price_rub'])

def calc():
    return str(round(calcEthCount()*calcEthRub(),2))






@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if message.text.lower()=='/balance':
        bot.send_message(message.chat.id, calc()+ ' руб.')

if __name__ == '__main__':
    bot.polling(none_stop=True)

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:07:06 2022

@author: jogeorg
"""

import robin_stocks as rs
import datetime;

#set robinhood_username=your_username_here
#set robinhood_password=your_password_here

ts = datetime.datetime.now()
fivepm = datetime.datetime.combine(
    datetime.date.today(), 
    datetime.time(17, 0))

rs.login(username=your_username,
         password=your_password,
         expiresIn=86400,
         by_sms=True)
if signal == True:
  rs.orders.order_buy_crypto_by_price('ETH', 
                                 1000,
                                 timeInForce='gtc')

if ts == fivepm:
  rs.orders.order_sell_crypto_by_price('ETH', 
                                 1000,
                                 timeInForce='gtc')
rs.logout()
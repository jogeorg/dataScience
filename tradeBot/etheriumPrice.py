# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:13:15 2022

@author: jogeorg
"""
# Get Etherium Price
import pandas as pd
import yfinance as yf
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')
pd.options.display.float_format = '${:,.2f}'.format

# Get Etherium Prices
today = datetime.today().strftime('%Y-%m-%d')
start_date = '2016-01-01'
eth_df = yf.download('ETH-USD',start_date, today)
eth_df.tail()
eth_df.reset_index(inplace=True)

# Calculate the Price change per Day
eth_df['Delta'] = eth_df['Close'] - eth_df['Open']

# Replace change as 1 or 0
eth_df.loc[eth_df.Delta > 0, 'Delta'] = 1
eth_df.loc[eth_df.Delta < 0, 'Delta'] = 0
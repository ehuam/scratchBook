#! usr/bin/env/ python3

import pandas as pd
from collections import deque

ltc = pd.read_csv("WG_CB-Pro-2021-Sell-Buy-LTC-USD.csv")
ltc.assign(tax_basis = ltc["total"]/ltc["size"])

#  create queue structure
ltc_buy = deque()
ltc_sell

# add each row (data frame) into queue
    # split into buy and sell

for row in ltc.itertuples():
    if(row.side == "BUY"):
        ltc_buy.append(row)
    else:
        ltc_sell.append(row)

# write to a log what is being done

# Pop from left and do work to it. (Consider recursion)
    # subtract size of sell from size of buy
    # if difference is negative
        # popleft from buy
    # if difference is positive
        # append left to buy
    # continue down queue until empty
# append left
# create new dataframe of transactions
    # add columns (profit, block = buy.trade_id)


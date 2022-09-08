! usr/bin/env/ python3

import pandas as pd
from collections import deque

# read in file and create column
ltc = pd.read_csv("WG_CB-Pro-2021-Sell-Buy-LTC-USD.csv")
ltc = ltc.assign(tax_basis = ltc["total"]/ltc["size"])

# consider renaming columns
# trade_id = id
# created at = created
# size unit = unit
# price/fee/total unit = total
ltc.rename({"trade id": "id",
    "created at": "date",
    "size unit":"unit",
    "price/fee/total unit":"total"},
    axis ="columns", inplace=True) 

#  create queue structure
ltc_buy = deque()
ltc_sell = deque()

# add each row (data frame) into queue
    # split into buy and sell

for row in ltc.itertuples():
    if(row.side == "BUY"):
        ltc_buy.append(row)
    else:
        ltc_sell.append(row)

# write to a log what is being done
log = list()

# create new dataframe of transactions
# add columns (profit, block = list of buy.trade_id)
profit_loss = pd.DataFrame()

# Pop from left and do work to it. (Consider recursion)
    # if ltc_sell.size() is less than ltc_buy.size():
    cost = ltc_sell.size() * ltc_buy.tax_basis  
    profit = ltc_sell.total - cost
    
    # add to profit_loss

    # use Peek equivalent, don't pop
    # if difference is negative
        # popleft from buy
    # if difference is positive
        # append left to buy
    # continue down queue until empty
# append left


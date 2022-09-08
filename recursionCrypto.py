def calc_profit(buyQueue, sellQueue): 
     if(!sellQueue): 
         return 
     elif(sellQueue[0].size() < ltc_buy[0].size()): 
         sold = ltc_sell.popleft() 
         buy = ltc_buy.popleft() 
         cost = sold.size() * buy.tax_basis 
         profit = sold.total - cost 
         log.append(profit) 
         ltc_buy.append( buy.size - sold.size) 
     else: 
         sold = ltc_sell.popleft() 
         buy = ltc_buy.popleft() 
         cost = sold.size() * buy.tax_basis 
         profit = buy.size() - cost 
         log.append(profit) 
         ltc_sold.append( sold.size() - buy.size() ) 
         return calc_profit(que) 

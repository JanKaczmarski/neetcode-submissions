class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # store stock from previous days, if i-th stock price < last_price
        # update the last_price with the new stock
        # if i-th stock price is > last_price sell the stock on this day,
        # store the i-th stock price as last price

        res = 0
        last_price = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            if price < last_price:
                # always chose smaller stock for buying
                last_price = price
            elif price > last_price: # sell with profit
                res += price - last_price
                last_price = price
        
        return res
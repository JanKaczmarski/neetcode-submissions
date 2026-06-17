class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)

        span = 0
        i = len(self.prices) - 1
        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1

        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
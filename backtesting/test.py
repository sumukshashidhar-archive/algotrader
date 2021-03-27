# from portfolio import Portfolio

# p = Portfolio()
# p.inject(500)
# print(p.get_value())


from trader import Trader


t = Trader()
print(t.portfolio.liquid)
print(t.buy('TICK', 5))
print(t.sell('TICK', 1))
print(t.get_holdings())
print(t.get_pl())
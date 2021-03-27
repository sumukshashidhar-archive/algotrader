from stock import Stock
class Portfolio:

	def __init__(self):
		self.value = 0 # current value of the portfolio
		self.injected = 0 # the value injected into the portfolio
		self.pl = 0 # the proft-loss value
		self.liquid = 0 # liquid money to buy stocks and shares 
		self.holdings = [] # filled with stocks and shares
		pass


	def inject(self, funds):
		# a way to put in money/funds into the portfolio.
		# this is essentially the money invested into the portfolio
		self.injected += funds
		self.liquid += funds
		return


	def get_value(self):
		# a way to obtain the entire value of our portfolio, with liquid and stocks
		# v = value
		v = self.liquid
		for i in self.holdings:
			v += i.get_value()

		return v
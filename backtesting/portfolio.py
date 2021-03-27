from stock import Stock
class Portfolio:

	def __init__(self):
		self.value = 0 # current value of the portfolio
		self.injected = 0 # the value injected into the portfolio
		self.pl = 0 # the proft-loss values
		self.plarray = []
		self.liquid = 0 # liquid money to buy stocks and shares 
		self.holdings = {} # filled with stocks and shares
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
		for i in self.holdings.keys():
			v += self.holdings[i].get_value()

		return v


	

		"""
		Section needs to be planned before construction
		"""

	# def withdraw(self, requestamt):
	# 	# allows you to withdraw money from your portfolio
	# 	# this resets your pl statements as well, as the money in your account has changed
	# 	if self.liquid >= requestamt:
	# 		# enough funds exist for withdrawl
	# 		self.plarray.append(self.pl)



	# 	else:
	# 		return False, "Not enough liquidity for withdrawl"

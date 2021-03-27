import math
class Trader:

	def __init__(self):
		self.portfolio = None


	def get_quote(self, ticker):
		pass


	def buy(self, ticker, volume):
		current = self.get_quote(ticker)
		total = math.ceil(current*volume)
		if self.portfolio.liquid >= total:
			pass
		else:
			return False, f"Insufficient Value: \nFunds Required:{total} \n funds available: {self.portfolio.liquid}"
		pass


	def sell(self, ticker, volume):
		pass

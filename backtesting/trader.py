import math
from stock import Stock
class Trader:

	def __init__(self):
		self.portfolio = None


	def get_quote(self, ticker):
		return 500


	def buy(self, ticker, volume):
		current = self.get_quote(ticker)
		total = math.ceil(current*volume)
		if self.portfolio.liquid >= total:
			self.portfolio.liquid -= total
			try:
				self.portfolio.holdings[ticker].volume += volume
			except:
				self.portfolio.holdings[ticker] = Stock()
			return True, f"Bought {volume} shares of {ticker} for a total of {total}. New balance is {self.portfolio.liquid}"
		else:
			return False, f"Insufficient Value: \nFunds Required:{total} \n funds available: {self.portfolio.liquid}"
		return


	def sell(self, ticker, volume):
		current = self.get_quote(ticker)
		total = math.ceil(current*volume)
		self.portfolio.liquid += total
		# remove from list of stocks
		self.portfolio.holdings[ticker].volume -= volume
		return

import math
from stock import Stock
from portfolio import Portfolio
class Trader:

	"""
	This is the main trading api. We will use it to get ticker and price value data for our entire portfolio. 

	It will build upon the other two classes defined such as the stock class and the portfolio class for efficiency purposes. 

	It will mainly perform the following operations:
	Get Quotes
	Buy
	Sell
	"""

	def __init__(self):
		# use a default portfolio setting
		self.portfolio = Portfolio()
		self.portfolio.inject(1000)


	def get_quote(self, ticker):
		return 100


	def buy(self, ticker, volume):
		current = self.get_quote(ticker)
		total = math.ceil(current*volume)
		if self.portfolio.liquid >= total:
			self.portfolio.liquid -= total
			try:
				self.portfolio.holdings[ticker].volume += volume
			except:
				self.portfolio.holdings[ticker] = Stock(ticker, current, volume)
			finally:
				return True, f"Bought {volume} shares of {ticker} for a total of {total}. New balance is {self.portfolio.liquid}. Total volume of shares for {ticker} available now is {self.portfolio.holdings[ticker].volume}."
		else:
			return False, f"Insufficient Funds: \nFunds Required:{total} \n Funds available: {self.portfolio.liquid}"
		return


	def sell(self, ticker, volume):
		current = self.get_quote(ticker)
		total = math.ceil(current*volume)
		self.portfolio.liquid += total
		# remove from list of stocks
		try:
			self.portfolio.holdings[ticker].volume -= volume
		except:
			self.portfolio.holdings[ticker] = Stock(ticker, current, -volume)
		finally:
			return True, f"Sold {volume} shares of {ticker} for a total of {total}. New balance is {self.portfolio.liquid}. Total volume after sales is {self.portfolio.holdings[ticker].volume}"
		return

	def get_pl(self):
		# get our total portfolio value first
		v = 0
		for i in self.portfolio.holdings.keys():
			v += self.portfolio.holdings[i].volume*self.get_quote(i)
		v += self.portfolio.liquid
		return v - self.portfolio.injected, ((v - self.portfolio.injected)/self.portfolio.injected)*100

	def get_holdings(self):
		for i in self.portfolio.holdings.keys():
			print(i, self.portfolio.holdings[i].value_purchased, self.portfolio.holdings[i].volume)
		
		print(f'\n {self.portfolio.liquid}')

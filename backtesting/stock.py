class Stock:

	def __init__(self, ticker, value_purchased, volume):
		self.ticker = ticker
		self.value_purchased = value_purchased
		self.current_value = value_purchased
		self.volume = volume
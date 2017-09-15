# This helper class for testing if customer has a discount, calculating if success
# Description:
# A customer who has already bought for over 1000 euro, 
# gets a discount of 10% on the whole order.
class RuleOne:
	##
	# Test method
	# @param order Order instance
	# @param customer Customer instance
	# @return bool
	def test(self, order, customer):
		return customer.getRevenue() > 1000
	##
	# Calculate method
	# @param order Order instance
	# @param customer Customer instance
	# @return array
	def calc(self, order, customer):
		return {
			'discount': (float(order.getTotal()) / float(100)) * 10,
			'description': "A customer who has already bought for over 1000 euro, gets a discount of 10% on the whole order."
		}
# This helper class for testing if customer has a discount, calculating if success
# Description:
# For every products of category 'Switches' (id 2), 
# when you buy five, you get a sixth for free.
class RuleTwo:
	##
	# Test method
	# @param order Order instance
	# @param customer Customer instance
	# @return bool
	def test(self, order, customer):
		return False
	##
	# Calculate method
	# @param order Order instance
	# @param customer Customer instance
	# @return array
	def calc(self, order, customer):
		return 'case2'
# This helper class for testing if customer has a discount, calculating if success
# Description:
# If you buy two or more products of category 'Tools' (id 1), 
# you get a 20% discount on the cheapest product.
class RuleThree:
	##
	# Test method
	# @param order Order instance
	# @param customer Customer instance
	# @return bool
	def test(self, order, customer):
		quantity = 0
		for item in order.getItems():
			if int(item.getCategory()) is int(1):
				quantity += int(item.getQuantity())
		return quantity >= 2
	##
	# Calculate method
	# @param order Order instance
	# @param customer Customer instance
	# @return array
	def calc(self, order, customer):
		minimum = min([float(v.getPrice()) for v in order.getItems() if int(v.getCategory()) is int(1)]) 
		return {
			'discount': (float(minimum) / float(100)) * 20,
			'description': "If you buy two or more products of category 'Tools' (id 1), ou get a 20% discount on the cheapest product."
		} 


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
		return 'case1'
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
		return False
	##
	# Calculate method
	# @param order Order instance
	# @param customer Customer instance
	# @return array
	def calc(self, order, customer):
		return 'case3'

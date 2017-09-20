##
# Customer class.
class Customer:
	##
	# Constructor
	# @param customer_id Customer id.
	# @param name Customer name.
	# @param name Customer revenue.
	# @return nothing
	def __init__(self, customer_id, name, revenue):
		self.id = int(customer_id)
		self.name = name
		self.revenue = float(revenue)
	##
	# Get customer id
	# @return customer id
	def getId(self):
		return self.id
	##
	# Get customer's name
	# @return name of Customer.
	def getName(self):
		return self.name
	##
	# Get customer's revenue
	# @return name of Customer.
	def getRevenue(self):
		return self.revenue
	##
	# Function to return customer array
	# @return array.
	def toArray(self):
		return {
			'name': self.getName(),
			'revenue': self.getRevenue()
		}
##
# Order class.
# Note: need to manually add items to instance
# becouse this way is more fit purity
class Order:
	##
	# Constructor
	# @param order_id Order id.
	# @param customer_id Customer instance.
	# @param total Order total summ.
	# @return nothing
	def __init__(self, order_id, customer, total):
		self.order_id = int(order_id)
		self.customer = customer
		self.total = float(total)
		self.items = list()
	##
	# Get order id 
	# @return order id.
	def getOrderId(self):
		return self.order_id
	##
	# Get customer instance
	# @return customer instance.
	def getCustomer(self):
		return self.customer
	##
	# Get total summ of order
	# @return total.
	def getTotal(self):
		return self.total
	##
	# Get array of order products
	# @return total.
	def getItems(self):
		return self.items
	##
	# Set product item
	# @patam item should be instance of product class
	# @return nothing.
	def appendItem(self, item):
		self.items.append(item)
	##
	# Method to return order array
	# @return array.
	def toArray(self): 
		res = {
			'id': self.getOrderId(),
			'total': self.getTotal(),
			'customer': self.getCustomer().toArray(),
			'items': list()
		}
		for item in self.getItems():
			res['items'].append(item.toArray())
		return res
##
# Product getter.
class Product:
	##
	# Constructor
	# @param product_id Product id.
	# @param category_id Product category id.
	# @param price Product unit price.
	# @param description Product description.
	# @return nothing
	def __init__(self, product_id, category_id, price, quantity, total, description):
		self.id = product_id
		self.category_id = int(category_id)
		self.price = float(price)
		self.quantity = int(quantity)
		self.total = float(total)
		self.description = description
	##
	# Get product id
	# @return product id
	def getId(self):
		return self.id
	##
	# Get product category id
	# @return product category id
	def getCategory(self):
		return self.category_id
	##
	# Get unit price of product
	# @return product unit price
	def getPrice(self):
		return self.price
	##
	# Get product discription
	# @return product description
	def getDescription(self):
		return self.description
	##
	# Get product order quantity
	# @return product quantity
	def getQuantity(self):
		return self.quantity
	##
	# Get product order total
	# @return product total items
	def getTotal(self):
		return self.total
	##
	# Method to return product array
	# @return array.
	def toArray(self):
		return {
			'id': self.getId(),
			'category': self.getCategory(),
			'price': self.getPrice(),
			'quantity': self.getQuantity(),
			'total': self.getTotal(),
			'description': self.getDescription()
		}
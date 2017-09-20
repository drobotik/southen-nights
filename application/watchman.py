import json
from application.classes import Product, Customer, Order

JSONpath = { 
	'product' : './data/products.json',
	'order': './data/orders.json',
	'customer':'./data/customers.json'}
##
# This instanse needed for reading json files 
# to find suitable orders, customers, products. 
# If something is exists, relevant objects must be created.
class DataWatchman:
	##
	# This is common method to read json files and trying to searching objects by 'id'
	# @param path Path to json file.
	# @param ent_id Entity Id 
	# @return array|None
	def __search(self, dataType, ent_id):
		with open(JSONpath[dataType]) as file:    
			data = json.load(file)
		result = None
		for entity in data:
			if dataType is 'product':
				if entity['id'] == ent_id:
					result = entity
			elif int(entity['id']) is int(ent_id):
				result = entity
		return result
	##
	# This method for product searching
	# @param product_id string id of needed product
	# @return new Product instance
	def findProduct(self, product_id):
		d = self.__search('product', product_id)
		if d is not None:
			return Product(d['id'], d['category'], d['price'], d['description'])
	##
	# This function for customer searching
	# @param customer_id int or string int Id of needed customer
	# @return new Customer instance
	def findCustomer(self, customer_id):
		d = self.__search('customer', customer_id)
		if d is not None:
			return Customer(d['id'], d['name'], d['revenue'])
	##
	# This function for order searching
	# @param order_id Id of needed order
	# @return new Order instance
	def findOrder(self, order_id):
		d = self.__search('order', order_id)
		if d is not None:
			order = Order(d['id'], self.findCustomer(d['customer-id']), d['total'])
			# adding product items to order
			for item in d['items']:
				p = self.__search('product', item['product-id'])
				if p is not None:
					order.appendItem(Product(p['id'], p['category'], p['price'], 
						item['quantity'], item['total'], p['description']))
			return order
			
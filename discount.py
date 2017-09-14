#! /usr/bin/python 
import json
from application.watchman import DataWatchman
from application.rules import RuleOne, RuleTwo, RuleThree

watchman = DataWatchman()
customer = watchman.findCustomer(2)
order = watchman.findOrder(2)

if customer is None:
   	print 'Customer not found'
elif order is None:
	print 'Order not found'
else:
	discounts = list()
	for rule in [ RuleOne(), RuleTwo(), RuleThree() ]:
		if rule.test(order, customer) is True:
			discounts.append(rule.calc(order, customer))
	
	if len(discounts) is 0:
		print 'Today this customer without discounts'
	else:
		print json.dumps({
			'discounts': discounts,
			'order': order.toArray(),
			'customer': customer.toArray()
		})
 
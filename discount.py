#! /usr/bin/python 
import json, sys
from application.watchman import DataWatchman
from application.rules import RuleOne, RuleTwo, RuleThree

watchman = DataWatchman()
order = watchman.findOrder(sys.argv[1])

if order is None:
	print 'Order not found'
else:
	discounts = list()
	for rule in [ RuleOne(), RuleTwo(), RuleThree() ]:
		if rule.test(order) is True:
			discounts.append(rule.calc(order))
	
	if len(discounts) is 0:
		print 'Today this customer without discounts'
	else:
		print json.dumps({
			'discounts': discounts,
			#'order': order.toArray(),
		})
 
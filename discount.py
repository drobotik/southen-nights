#! /usr/bin/python 
import inspect
from application.watchman import DataWatchman
from application.discount import RuleOne, RuleTwo, RuleThree

watchman = DataWatchman()
customer = watchman.findCustomer(2)
order = watchman.findOrder(2)

if customer is None:
   	print 'Customer not found'
elif order is None:
	print 'Order not found'
else:
	print 'qaz'

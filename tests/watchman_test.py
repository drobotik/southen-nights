# -*- coding: utf-8 -*-

import unittest
from application.watchman import DataWatchman
watchman = DataWatchman()

class TestDiscountResults(unittest.TestCase):

	def test_methodsWithoutArgument(self):
		self.assertEquals(watchman.findProduct(), None)
		self.assertEquals(watchman.findCustomer(), None)
		self.assertEquals(watchman.findOrder(), None)

	def test_methodsWithWrongArgument(self):
		self.assertEquals(watchman.findProduct(345657), None)
		self.assertEquals(watchman.findProduct('\\'), None)
		# print type('€') # encoding cases begins from here :D
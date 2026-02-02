#!/usr/bin/python3
"""Module than define a list"""


class MyList(list):
	"""define a list"""
	
	def print_sorted(self):
		"""print sorted list"""
		print(sorted(self))

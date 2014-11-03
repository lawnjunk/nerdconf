#!/usr/bin/python

class Conf:
	def __init__(self):
		self.file_name
		self.full_path
		self.os

	def __init__(self, file_name, full_path, os):
		self.file_name = file_name
		self.full_path = full_path
		self.os = os

var conf_files = [CONF()}

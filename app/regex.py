import re

class Package:
	def __init__(self, name, depends, description):
		self.name = name
		self.depends = depends
		self.description = description
		self.rdepends = []

	def __str__(self):
		return str(self.name) + '\n' + self.description + '\n' + str(self.depends) + '\n' + str(self.rdepends)

def search_rdepends(packages_object):
	for package1 in packages_object:
		name = getattr(package1, 'name')
		rdepends = getattr(package1, 'rdepends')
		for package2 in packages_object:
			if name in getattr(package2, 'depends'):
				rdepends.append(getattr(package2, 'name'))

def regex():
	try:
		file = open('/var/lib/dpkg/status', 'r')
	except IOError:
		file = open('../status.real', 'r')
	# regex to use:
	# ^Package:\s(.+?(?=\n[^\s]))
	# ^Depends:\s(.+?(?=\n[^\s]))
	# ^Description:\s(.+?(?=\n[^\s]))

if __name__ == '__main__':
	regex()
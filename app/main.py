import re
from flask import Flask, render_template

app = Flask(__name__)

class Package:
	def __init__(self, name, depends, description):
		self.name = name
		self.depends = depends
		self.description = description
		self.rdepends = []

	def __str__(self):
		return str(self.name) + '\n' + str(self.description) + '\n' + str(self.depends) + '\n' + str(self.rdepends)

def parse_depends(depends):
	names = []
	if depends == None:
		return names
	for separatedByPipe in depends.split(' | '):
		for separatedByComma in separatedByPipe.split(', '):
			names.append(separatedByComma.split(' ')[0])
	return names

def search_rdepends(packages_object):
	for package1 in packages_object:
		name = getattr(package1, 'name')
		rdepends = getattr(package1, 'rdepends')
		for package2 in packages_object:
			if name in getattr(package2, 'depends'):
				rdepends.append(getattr(package2, 'name'))

def regex_packages():
	try:
		file = open('/var/lib/dpkg/status', 'r')
	except IOError:
		try:
			file = open('status.real', 'r')
		except IOError:
			raise SystemExit
	regex = []
	regex.append(re.compile(r'^Package:\s(.+?(?=\n\S))', re.MULTILINE | re.DOTALL))
	regex.append(re.compile(r'^Depends:\s(.+?(?=\n\S))', re.MULTILINE | re.DOTALL))
	regex.append(re.compile(r'^Description:\s(.+?(?=\n\S))', re.MULTILINE | re.DOTALL))
	packages_raw = file.read().split('\n\n')
	packages_object = []
	for package in packages_raw:
		if package == '':
			continue
		package += '\nend'
		found = []
		for entry in regex:
			match = entry.search(package)
			if match:
				found.append(match.group(1))
			else:
				found.append(None)
		packages_object.append(Package(found[0], parse_depends(found[1]), found[2]))
	search_rdepends(packages_object)
	packages_object.sort(key=lambda package: package.name)
	file.close()
	return packages_object

global packages_object
packages_object = regex_packages()

@app.route('/')
def display_all():
	return render_template('index.html', packages=packages_object)

@app.route('/<string:name>')
def display_info(name):
	for package in packages_object:
		if getattr(package, 'name') == name:
			return render_template('info.html', package=package)
	return 'Error :('

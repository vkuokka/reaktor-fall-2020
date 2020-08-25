import re
from flask import Flask, render_template

app = Flask(__name__)

class Package:
	def __init__(self, name, dependencies, description):
		self.name = name
		self.dependencies = dependencies
		self.description = description
		self.reverseDependencies = []

	def __str__(self):
		return str(self.name) + '\n' + str(self.description) + '\n' \
		+ str(self.dependencies) + '\n' + str(self.reverseDependencies)

def parse_dependencies(dependencies):
	names = []
	if dependencies is not None:
		for separatedByPipe in dependencies.split(' | '):
			for separatedByComma in separatedByPipe.split(', '):
				names.append(separatedByComma.split(' ')[0])
	return names

def search_reverse_dependencies(packages_object):
	for package1 in packages_object:
		for package2 in packages_object:
			if package1.name in package2.dependencies:
				package1.reverseDependencies.append(package2.name)

def regex_packages():
	try:
		file = open('/var/lib/dpkg/status', 'r')
	except IOError:
		try:
			file = open('status.real', 'r')
		except IOError:
			raise SystemExit
	packages_raw = file.read().split('\n\n')
	file.close()
	regexList = [
	re.compile(r'^Package:\s(.+?(?=\n\S))', re.MULTILINE | re.DOTALL),
	re.compile(r'^Depends:\s(.+?(?=\n\S))', re.MULTILINE | re.DOTALL),
	re.compile(r'^Description:\s(.+?(?=\n\S))', re.MULTILINE | re.DOTALL)
	]
	packages_object = []
	for package in packages_raw:
		if 'Package: ' in package:
			package += '\nEOF' # String must end with alphabetical value in order to regex work correctly.
			values = []
			for regexObject in regexList:
				regexMatch = regexObject.search(package)
				if regexMatch:
					values.append(regexMatch.group(1))
				else:
					values.append(None)
			packages_object.append(Package(values[0], parse_dependencies(values[1]), values[2]))
	search_reverse_dependencies(packages_object)
	packages_object.sort(key=lambda package: package.name)
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

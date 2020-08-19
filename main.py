class Package:
	def __init__(self):
		self.name = None
		self.description = None
		self.depends = []
		self.rdepends = []
	def __str__(self):
		return(self.name + '\n' + str(self.depends) + '\n' + str(self.rdepends) + '\n' + self.description)

def parse_depends(line):
	names = []
	separated = line.split(', ')
	for separate in separated:
		names.append(separate.split(' ')[0])
	return names
def search_rdepends(packages_object):
	for package1 in packages_object:
		name = getattr(package1, 'name')
		rdepends = getattr(package1, 'rdepends')
		for package2 in packages_object:
			if name in getattr(package2, 'depends'):
				rdepends.append(getattr(package2, 'name'))
def main():
	file = open('status.real', 'r')
	packages_raw = file.read().split('\n\n')
	packages_object = []
	for package_raw in packages_raw:
		if package_raw == '':
			continue
		lines = package_raw.split('\n')
		package = Package()
		for line in lines:
			name_field = line.split(': ')
			if name_field[0] == 'Package':
				setattr(package, 'name', name_field[1])
			elif name_field[0] == 'Description':
				setattr(package, 'description', name_field[1])
			elif name_field[0][0] == ' ':
				setattr(package, 'description', str(getattr(package, 'description')) + ' \n' + name_field[0])
			elif name_field[0] == 'Depends':
				setattr(package, 'depends', parse_depends(name_field[1]))
		packages_object.append(package)
	search_rdepends(packages_object)
	for package in packages_object:
			print(package)
	file.close()

if __name__ == '__main__':
	main()
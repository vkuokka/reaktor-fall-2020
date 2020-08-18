class Package:
	def __init__(self):
		self.name = None
		self.description = None
		self.depends = None
		self.reverse_depends = None

def main():
	file = open('status.real', 'r')
	packages_raw = file.read().split('\n\n')
	for package_raw in packages_raw:
		if package_raw == '':
			continue
		package = Package()
		lines = package_raw.split('\n')
		for line in lines:
			name_field = line.split(': ')
			if name_field[0] == 'Package':
				setattr(package, 'name', name_field[1])
			elif name_field[0] == 'Description':
				setattr(package, 'description', name_field[1])
			elif name_field[0] == 'Depends':
				setattr(package, 'depends', name_field[1])
			elif name_field[0][0] == ' ':
				setattr(package, 'description', str(getattr(package, 'description')) + name_field[0])
		print(getattr(package, 'description'))
	file.close()

if __name__ == '__main__':
	main()
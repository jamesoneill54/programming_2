def build_dictionary(filename):
	mappings = dict()
	try:
		with open(filename, "r") as f:
			for line in f:
				[key, value] = line.strip().split()
				mappings[key] = int(value)
	except FileNotFoundError:
		pass
	return mappings

def extract_range(d, low, high):
	new_dict = dict()
	for (key, value) in d.items():
		if low <= value <= high:
			new_dict[key] = value
	return new_dict

def main():
	d = build_dictionary('mappings_52.txt')
	nd = extract_range(d, 5, 15)
	for (key, value) in sorted(nd.items()):
		print('{} : {}'.format(key, value))

if __name__ == '__main__':
	main()
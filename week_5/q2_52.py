import sys

def main():
	d = dict()
	word_list = [line.strip() for line in sys.stdin.read()]
	for char in word_list:
		if char in d:
			d[char] += 1
		else:
			d[char] = 1
	a = []
	for (key, value) in d.items():
		if value == 1:
			a.append(key)

	for char in word_list:
		if char in a:
			print(char)

if __name__ == "__main__":
	main()
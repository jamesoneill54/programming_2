import sys

def main():
	s = list(sys.argv[1])
	n = int(sys.argv[2])

	for char in range(1, n+1):
		li = s.pop()
		s.insert(0, li)

	print("".join(s))

if __name__ == "__main__":
	main()
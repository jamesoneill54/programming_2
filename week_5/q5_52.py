import sys

def get_mean(a):
    mean = sum(a) / len(a)
    return mean

def main():
    nums = [int(line.strip()) for line in sys.stdin]
    mean = get_mean(nums)
    total = 0
    for num in nums:
        distance_to_mean = abs(num - mean) ** 2
        total += distance_to_mean
    n = total / (len(nums) - 1)
    std_dev = n ** 0.5
    print("Standard deviation: {:.3f}".format(std_dev))

if __name__ == "__main__":
    main()
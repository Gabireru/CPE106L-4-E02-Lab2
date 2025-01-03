#PostLab1

'''
A group of statisticians at a local college has asked you to create a set of functions that compute the median and mode of a set of numbers,
as defined in the below sample programs:
mode.py
median.py

Define these functions in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers.
Each function should expect a list of numbers as an argument and return a single number.
Each function should return 0 if the list is empty.
Include a main function that tests the three statistical functions with a given list.
'''

from collections import Counter

def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def mode(numbers):
    if not numbers:
        return 0
    frequency = Counter(numbers)
    max_count = max(frequency.values())
    modes = [key for key, count in frequency.items() if count == max_count]
    if len(modes) == 1:
        return modes[0]
    return modes 

def main():
    print("If List is not Empty")
    data = [1, 2, 2, 3, 4, 5, 5, 5]
    print(f"Mean: {mean(data)}")
    print(f"Median: {median(data)}")
    print(f"Mode: {mode(data)}")
    print("If List is Empty")
    data = []
    print(f"Mean: {mean(data)}")
    print(f"Median: {median(data)}")
    print(f"Mode: {mode(data)}")

if __name__ == "__main__":
    main()

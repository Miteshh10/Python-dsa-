def find_smallest(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest


numbers = [45, 12, 78, 3, 29]

print("Smallest number:", find_smallest(numbers))
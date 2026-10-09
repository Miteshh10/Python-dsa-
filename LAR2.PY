def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        # If num is greater than largest,
        # update largest
        if num > largest:
            largest = num

    return largest


numbers = [10, 25, 7, 89, 34]
print("Largest number:", find_largest(numbers))
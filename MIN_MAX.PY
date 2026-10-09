def find_max_min(numbers):
    if not numbers:
        return None, None

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum, minimum


numbers = [10, 25, 7, 89, 34]

maximum, minimum = find_max_min(numbers)

print("Maximum:", maximum)
print("Minimum:", minimum)
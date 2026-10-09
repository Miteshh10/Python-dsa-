def second_largest(numbers):
    unique_numbers = set(numbers)

    if len(unique_numbers) < 2:
        return None

    largest = float("-inf")
    second = float("-inf")

    for num in unique_numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num

    return second


numbers = [10, 25, 7, 89, 34]

print("Second largest:", second_largest(numbers))
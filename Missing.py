def find_missing(numbers):
    n = len(numbers) + 1

    for num in range(1, n + 1):
        if num not in numbers:
            return num

    return None


numbers = [1, 2,3, 4, 5, 6]

print("Missing number:", find_missing(numbers))
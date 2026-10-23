def calculate_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


numbers = [10, 20, 20, 40, 50]

print("Sum =", calculate_sum(numbers))
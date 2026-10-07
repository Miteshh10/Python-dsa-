def sum_digits(n):
    TOTAL = 0

    while n > 0:
        LS = n % 10
        TOTAL = TOTAL + LS
        n = n // 10

    return TOTAL


n = int(input("Enter the number: "))

print("Total is:", sum_digits(n))
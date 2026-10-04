# count the digit 
def digit(n):
    n = abs(n)

    if n == 0:
        return 1

    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count


num = int(input("Enter a number: "))

print("Number of digits:", digit(num))


# logarithim method to count digits

# log10(num)
# log10(123)= 2.089905111439398 + 1 = 3.089905111439398

# time complexity of this method is O(log10(n)) and space complexity is O(1)

# when iterative is done not specfic number use that number in time complexity 
# example : 10 -> O(log10(n))
# 2 -> O(log2(n))
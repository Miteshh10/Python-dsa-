def pali(n):

    original = n
    res = 0

    while n > 0:
        digit = n % 10
        res = res * 10 + digit
        n = n // 10

    if original == res:
        return "PALINDROME"
    else:
        return "NOT PALINDROME"


num = int(input("Enter the number: "))

print("RESULT:", pali(num))
l1 = [1, 2, 3]
l2 = [3, 4, 5]

i = len(l1) - 1
num1 = 0
num2 = 0

while i >= 0:
    num1 = num1 * 10 + l1[i]
    num2 = num2 * 10 + l2[i]
    i -= 1

print(num1)
print(num2)
print(num1 + num2)
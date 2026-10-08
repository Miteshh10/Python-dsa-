def fact(n):

    result=1
    for i in range ( 1, n+1):
      result = result * i
    return result

num = int( input("Enter the number : "))

print("dactorial of the number is :" , fact(num))
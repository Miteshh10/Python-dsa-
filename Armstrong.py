def arm(n):
    original = n
    count = 0 
    nod = len(str(n))

    while n > 0:
         digit = n%10
         count = count + ( digit** nod)

         n= n//10

    if original == count:
        return "ARMSTRONG"
    else:
        return "NOT ARMSTRONG"
         
num = int(input("enter the number: "))

print("Result :" ,arm(num))
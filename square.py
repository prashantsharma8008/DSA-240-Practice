n= int(input("Enter the Digit"))
digit = 0
while n>0:
    digit = digit + n%10*n%10
    n = n//10
print(digit)
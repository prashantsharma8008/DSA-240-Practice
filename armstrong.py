n = int(input("Enter the digits to check if it is Armstrong number or not"))
# a*3+b*3+c*3 = abc hence its a armstrong number
digit = 0
while n>0:
    digit = digit +(n%10)**3
    n = n//10
print(digit)
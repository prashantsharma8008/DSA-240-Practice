n = int(input("Enter the digit"))
digit = 0
while n>0:
    digit = (digit * 10) + n%10
    n = n // 10
print(digit)

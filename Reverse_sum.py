n = int(input("Enter the Digits"))
digit = 0
while n>0:
    digit = digit*10 + n%10
    n = n//10
print(digit)
if digit == n:
    print(False)
else:
    print(True)
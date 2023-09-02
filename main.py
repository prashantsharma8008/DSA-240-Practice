i = int(input("Enter the digit"))
num = 0
while i>0:
	num = num + i%10*i%10*i%10
	i= i//10
print(num)
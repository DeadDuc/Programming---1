variable = int(input("Enter test number: "))
sum = 0
i = 0
while(sum < variable):
	i += 2
	sum += i
	print(i)
	if sum == variable or sum >= variable:
		break

input()
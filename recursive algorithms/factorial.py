# This following code calculates the factorial of a number using recursive method.
# A recursive algorithm has two case: a base case and a recursive case

def factorial(num):
	if num < 2:                               # base case
		return 1
	else:                                     # recursive case
		return num * factorial(num-1)         

num = int(input('Enter the number: '))
ans = factorial(num)
print('The factorial of', num, 'is', ans)
#project-1 Simple calculator


num1 = float(input('Enter first number: '))
op = input('Enter operators (+, -, *, /): ')
num2 = float(input('Enter second number: '))

if op == '+':
	print('The sum of numbers is:', num1 + num2)
elif op =='-':
	print('The substraction of numbers is:', num1 - num2)
elif op =='*':
	print('The multi of numbers is:', num1 * num2)
elif op =='/':
	if num2 != 0:
		print(num1 / num2)
	else:
		print("Error,not divisible!")
else:
	print('Invalid!')

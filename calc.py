def calculator():
	print("Simple Calculation.")
	print("Operations: +, -, *, /")

	try:
		num1 = float(input("Enter first number: "))
		op = input("Enter operation(+, -, *, /): ")
		num2 = float(input("Enter second number: "))

		if op == "+":
			result = num1 + num2
			print(f'{num1} + {num2} = {result}')
		elif op == "-":
			result = num1 - num2
			print(f'{num1} - {num2} = {result}')
		elif op == "*":
			result = num1 * num2
			print(f'{num1} * {num2} = {result}')
		elif op == "/":
			if num2 == 0:
				print("Error: Cannot divide by Zero!")
			else:
				result = num1 / num2
			print(f'{num1} / {num2} = {result}')
	except ValueError:
		print("Error: Please enter valid numbers!")

calculator()

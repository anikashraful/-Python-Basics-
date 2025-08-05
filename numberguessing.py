import random

secret = random.randint(1,10)
guess = None


while guess != secret:
	guess = int(input('Guess a number (1-10): '))
	if guess < secret:
		print("Too low!")
	elif guess > secret:
		print('Too high!')
	else:
		print('Got it! Success.')

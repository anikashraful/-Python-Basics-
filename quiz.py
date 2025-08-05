print('Welcome to the quiz!')

questions = [
    {'q': 'what is 2 + 2?', 'ans': '4'},
    {'q': "what data type is 'hello'?", 'ans': 'string'},
    {'q': 'which loop runs indefinitely?', 'ans': 'while'}
]

score = 0

for q in questions:
    answer = input(q['q'] + ' ')
    if answer.lower() == q['ans']:
        print('Correct!')
        score = score + 1
    else:
        print('Wrong!')

print(f'You scored {score}/{len(questions)}')
students = []

#collect data from 3 students

for i in range(3):
	name = input('Enter name: ')
	age = input('Enter age: ')
	grade = input('Enter grade: ')
	student = {'Name': name, 'Age': age, 'Grade': grade}
	students.append(student)

print(students)
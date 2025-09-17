responses = [] # List to store all responses
unique_emails = set() # Set to track unique emails


for i in range(3):
	name = input('Name: ')
	email = input('Email: ')
	age = input('Age: ')
	response = {'Name': name, 'Age': age, 'Email': email}
	responses.append(response)
	unique_emails.add(email)


print('All responses:',responses)
print('Unique emails:',unique_emails)
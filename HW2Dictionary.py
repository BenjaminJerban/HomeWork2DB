#Home work 2 Question1

users_count = int(input("Enter the count of users : "))
users = []

for x in range(users_count) :
	username = input("Enter user.name :")	
	user_age = int(input("Enter user.age :"))
	users.append({"name" : username, "age" : user_age})
	
print(users)

user_search = input("Enter the name to search : ")

counter = 0
for search in users :
	counter+=1
	if user_search == search["name"]:
		print (search["age"])
		break
	elif user_search != search["name"] and counter == users_count:
		print ("No such User")

































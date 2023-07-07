
no_of_users=int(input("How many users to add: "))

user_list=[]

while no_of_users > 0:
    user = (input("Enter Name: "))
    user_list.append(user)
    no_of_users-=1
    print(no_of_users)

print(user_list)
import boto3

client = boto3.client('iam')

def create_user():
    response = client.create_user(
        UserName= input("ENTER USERNAME: "),

    )

def create_group():
    response = client.create_group(
    GroupName=input("ENTER GROUPNAME: ")
)

def add_user_to_group():
    response = client.add_user_to_group(
    GroupName=input('ENTER GROUPNAME: '),
    UserName=input('ENTER USERNAME: ')
)

def list_group():
    response = client.list_groups()
    grp = response["Groups"]
    for i in range(len(grp)):
        dict1 = grp[i]
        print(dict1["GroupName"])

def list_users():
    response = client.list_users()
    #print(response)
    usr = response["Users"]
    #for i in range(len(usr)):
    #    dict1 = usr[i]
    #    print(dict1["UserName"])
    length = len(usr)
    i = 0
    while length > 0:
        dict1 = usr[i]
        print(dict1["UserName"])
        length-=1
        i+=1
        
while True:
    print("            ")
    print("1. List of Users")
    print("2. List of Groups")
    print("3. Create user")
    print("4. Create group")
    print("5. Add user into a Group")
    print("0. Exit")

    choice = int(input("ENTER CHOICE: "))

    if choice==1:
        list_users()
    elif choice==2:
        list_group()
    elif choice==3:
        create_user()
    elif choice==4:
        create_group()
    elif choice==5:
        add_user_to_group()
    elif choice==0:
        break
    else:
        print("INVALID CHOICE")
        continue
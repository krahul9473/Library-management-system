#Code for  student
print("Enter your roll number")
while True:
    try:
        roll=int(input())
    except NameError, ValueError:
        continue
print ("Enter your password")
password=input()

# If username and password present in database, welcome them

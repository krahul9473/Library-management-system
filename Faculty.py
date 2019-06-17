#Code for faculty
#Code for  student
print("Enter your employee number")
while True:
    try:
        emp_no=int(input())
    except NameError, ValueError:
        continue
print ("Enter your password")
password=input()

# If username and password present in database, welcome them



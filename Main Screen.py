import pandas as pd
from datetime import datetime
from Sudent import Student
from Faculty import Faculty

print("Welcome to the Library.")
print("Please Choose from the following \n")
print(" 1. Student")
print(" 2. Faculty")
print(" 3. Library Staff")
print(" 4. Library Rules \n")
now=datetime.now()
print ("%02d-%02d-%04d\t%02d:%02d:%02d\n" %(now.day, now.month, now.year, now.hour, now.minute, now.second))
#This will give a static time. Perhaps somehow, can we make it live

class User(object):
    def __init__(self, ID, password):
        self.ID=ID
        self.password=password
    def issueBook(self, bookNum):
        pass
    def reissueBook(self, bookNum):
        pass
    def returnBook(self, bookNum):
        pass

while True:
    try :
        choice = int(input("Enter the index please \n"))

    except ValueError:
        print("Sorry, enter a valid response \n")

    else :
        if choice in ([1,2,3,4]):
            break
    
    if choice == 1:
        print("Enter your student roll number: \n")
        r_num = input()

        print("Enter your password : \n")
        key = input()

        csv_path = 'Student.csv'

        df = pd.read_csv(csv_path)
        
        #still need to add further code for authentication

        #if authenticated:-
        st=Student(r_num, key)
        st.runStudentModule() #do all required procedures here
    elif choice==2:
        print("Enter your employee number: \n")
        emp_num = input()

        print("Enter your password : \n")
        key = input()

        csv_path = 'Faculty.csv'

        df = pd.read_csv(csv_path)
        
        #still need to add further code for authentication

        #if authenticated:-
        fac=Faculty(emp_num, key)
        st.runFacultyModule() #do all required procedures here
    
        

    





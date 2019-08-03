from datetime import datetime
from Sudent import Student
from Faculty import Faculty
import sqlite3

connection1=sqlite3.connect("Student.db")
connection2=sqlite3.connect("faculty.db")

#cursor objects
cursor1=connection1.cursor()
cursor2=connection2.cursor()

# execute only once
cursor1.execute("CREATE TABLE Student(RollNo INT,Password Text,Name TEXT)")
cursor2.execute("CREATE TABLE faculty(EmployeeNumber INT,Name TEXT,BooksIssued INT,Password TEXT)")

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
        #checking rollno
        cursor1.execute("SELECT Password FROM Student WHERE RollNo={}".format(r_num))
        
        #checking if roll number in database
        j=cursor1.fetchone()
        if(j[0]==None):
                       
            print("This roll number doesn't exist")
            
        elif(key ==j[0]): #if password is correct
            st=Student(r_num, key)
            st.runStudentModule() #do all required procedures here
        
        
    elif choice == 2:
        print("Enter your employee number: \n")
        emp_num = input()

        print("Enter your password : \n")
        key = input()
        
        cursor2.execute("SELECT Password FROM  faculty WHERE EmployeeNumber='{}'".format(emp_num))
        k=cursor2.fetchone()
        if(k[0]==None):
            print("This employee number does not exist")
        elif(key==k[0]):
            #code for correct password
        
        #still need to add further code for authentication
        #if authenticated:-
            fac=Faculty(emp_num, key)
            fac.runFacultyModule() #do all required procedures here
     
    elif choice == 3:
        print ("Library admin password")
        password=input()
        #if password matches the one in database
            libstaff=LibSatff()
            libstaff.runLibStaffModule()
            
    else:
        print('''\t\t\t\tLIBRARY RULES
        1. Books are issued for a period of 7 days for students and 15 days for faculty.
        2. Fine for overdue books is Rs. 10 per day.
        3. Maximum reissues allowed are 3 for students and 5 for faculty''')
        
        
        
    
        
connection1.commit()
connection2.commit()
    





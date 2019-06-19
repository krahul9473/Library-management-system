import Main Screen
class Student(User):

    #init of User derived, so no need for init again
    def runStudentModule():
        

            print("Enter your student roll number: \n")
            r_num = input()

            print("Enter your password : \n")
            key = input()

            csv_path = 'Student.csv'

            df = pd.read_csv(csv_path)
            
            #still need to add further code for authentication

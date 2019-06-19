import Main Screen
class Faculty(User):

    #init of User derived, so no need for init again
    def runFacultyModule():
        

            print("Enter your student employee number: \n")
            r_num = input()

            print("Enter your password : \n")
            key = input()

            csv_path = 'Faculty.csv'

            df = pd.read_csv(csv_path)
            
            #still need to add further code for authentication
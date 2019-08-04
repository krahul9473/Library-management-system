import Main Screen
class Faculty(User):
    issuePeriod=15
    maxReissues=5

    def suggestBook(self):

    def runFacultyModule(self):
        print ("Welcome, " + ) #Put the name from database here
        print('''What would you like to do?
        1. Issue new book
        2. Reissue a book
        3. Return a book
        4. Suggest a new book for department''')
        
        
    option=int(input("Enter choice"))
        
        
        if(choice==1):
            
            
            name=input("Enter book name to issue")
            cursor.execute('SELECT * FROM books WHERE Name="{}"'.format(name))
            a=cursor.fetchone()
            if(a[0]==None):
                print("No book in records")
            elif(a[3]=='A'):
                      
                cursor.execute('UPDATE  books SET status="I" WHERE  Name="{}"'.format(name))
                print("Book issued")
         
        elif(choice==2):
            pass
        
        
        elif(choice==3):
            
            name=input("Enter book name to return")
            cursor.execute('UPDATE books SET status="A" WHERE Name="{}"'.format(name))
            print("book returned") 
        
            

            

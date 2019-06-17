#Code for the main screen
print('''Welcome to the library. Choose from below\n
      1.Student
      2. Faculty
      3. Library staff
      4. Read Library Rules''')
while True:
    try:
        choice=int(input())
    except NameError, ValueError:
        continue
    if(choice in [1, 2, 3, 4]):
        break;

    



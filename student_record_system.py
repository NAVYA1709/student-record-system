with open("StudentsRecord.txt","a") as file : # If file doesn’t exist → creates it, If file exists → does nothing, Writes no junk text
    pass
while(True) :
    print("MENU")
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Exit")
    print("5.Clear Records")
    try:
        choice = int(input("Enter choice : "))
        if choice == 1 :
                name = input("Enter name : ")
                age = int(input("Enter age : "))
                marks = float(input("Enter marks : "))
                with open("StudentsRecord.txt","a") as file :
                    file.write(f"Name : {name}\n Age : {age}\n Marks : {marks}\n\n")
        elif choice == 2 :
                with open("StudentsRecord.txt","r") as file :
                    content = file.read()
                    print(content)
        elif choice == 3 :
                stuName=input("Enter student Name : ")
                found=False
                with open("StudentsRecord.txt","r") as file :
                    for line in file :
                        if stuName in line: # Because it checks: “Is Amal inside Name: Amal?”
                            found=True
                            print("Record found!")
                            print(line)
                if not found :                                  #IF CONDITION TRUE AITHE!!! IF NOT FALSE -> TRUE THEN PRINT
                     print("Not found!")
        elif choice == 4 :
                print("program ends\n")
                break
        elif choice == 5:
            with open("StudentsRecord.txt", "w") as file:
                pass
            print("All records cleared")
        else :
                print("Invalid number chosen , please check again.")
    except ValueError:
        print("Invalid value entered!!CHECK AGAIN")


        






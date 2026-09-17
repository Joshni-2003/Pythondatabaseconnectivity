from operations import add_emp,view_emp,update_emp,delete_emp
while True:
    
    print("1. add employee")
    print("2. view employee")
    print("3. update employee")
    print("4. delete employee")
    print("5. exit")
    choice=int(input("enter a option:"))
    if choice==1:
        add_emp()
    elif choice==2:
        view_emp()
    elif choice==3:
        update_emp()
    elif choice==4:
        delete_emp()
    else:
        print("exit")
from db import get_connection
# connection=get_connection()  # global variables we use anywhere
# cur=connection.cursor()


def add_emp():
    # print("add employee")
    emp_name=input("enter a empname:")
    emp_sal=float(input("enter a salary:"))
    emp_dept=input("enetr a department:")
    emp_loc=input("enter a location:")
    connection=get_connection()
    cur=connection.cursor()  # cursor is an object to communicate with db.
    cur.execute("insert into employeemanagementsystem(name,salary,dept,location)values(%s,%s,%s,%s)",(emp_name,emp_sal,emp_dept,emp_loc))
    connection.commit()  # when we use commit --- data add chesthunnapudu database lo then we use commit
    connection.close()
    print(f"{emp_name} added successfully")

def view_emp():
    # print("view employee")
    connection=get_connection()
    cur=connection.cursor()
    cur.execute("select * from employeemanagementsystem")
    
    # print(cur.fetchall())  # list of tuples #it is list we will iterate them 
    data=cur.fetchall()
    for i in data:
            print(i[1])
    connection.close()
    print("employees data fetched successfully")

def update_emp():
    connection=get_connection()
    cur=connection.cursor()
    id=int(input("enter a id which u want to update:"))
    name=input("enter a emp name:")
    sal=float(input("enter a sal:"))
    dept=input("enter a dept:")
    loc=input("enter a location:")
    cur.execute("update employeemanagementsystem set name=%s,salary=%s,dept=%s,location=%s where id=%s",(name,sal,dept,loc,id))
    
    connection.commit()
    connection.close()
    if cur.rowcount > 0:
        print("Emp updated successfully")
    else:
        print("Employee ID not found")


    # print("employee updated successfully")


def delete_emp():
     connection=get_connection()
     cur=connection.cursor()
     emp_id=int(input("enetr employee id:"))
     cur.execute("delete from employeemanagementsystem where id=%s",(emp_id,))
     connection.commit()
     connection.close()
     print("emp deleted successfully")



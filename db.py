# python---database--->mysql-connector-python (it is not an inbulit fn.it is third party modile. we have to import)
# pip install mysql-connector-python


import mysql.connector
print(mysql.connector)
def get_connection():
    connect= mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="pdbc"
    )
    return connect
# print("database connected successfuly")  # if there is an error occurs it does not print database connected successfully because python is interpreted lang


# qn:how can we check and validate:mysql.connector(third-party installed in your local) .workbench-laptop,vscode -laptop----mysql.connectors jumps from one software to another
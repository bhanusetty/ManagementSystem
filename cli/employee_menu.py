from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB

#this obj for employee repo
emp_db = EmployeeDB()
#this is object of employee auth
emp_auth = EmployeeAuthentication(emp_db)

#this function for signup new employee
def employeeSignup():
    print('employee signup')
    name = input('enter your name:')
    email = input('enter your email')
    password = input('enter your password')
    emp_auth.createEmployee(name,email,password)

def employeeLogin():
    print('employee Login')
    
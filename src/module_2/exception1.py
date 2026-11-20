class invalidSalary(Exception):
    pass
 
def calSalary(salary):
    if salary <= 0:
        raise invalidSalary("Invalid Salary Processed")
 
    print("Salary: ", salary)
 
try:
    calSalary(100)
except invalidSalary as error:
    print("Error: ",error)
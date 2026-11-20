from dataclasses import dataclass

@dataclass
class Employee:
    emp_name:str
    dept:str
    emp_id:int

employee=Employee("Khyrati","SE",90337)

print(employee)
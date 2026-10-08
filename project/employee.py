# Create an employee management system using all four OOP concepts. Create a
# parent Employee class with private salary and common employee details.
# Create Developer and Manager child classes. Both should have
# a calculate_salary() method but calculate the salary differentl



class employee:
    def __init__(self,name,department,salary):
    
        self.name=name
        self.department= department
        self.salary=salary

    def get_salary(self):
        return self.salary
    
    def display(self):
        print("name:",self.name)
        print("department:",self.department)
        print("psalary:",self.salary)


class devoloper(employee):
    def calculate_salary(self):
           return self.get_salary() + 5000
class manager(employee):
    def calculate_salary(self):
        return self.get_salary() + 10000

devoloper1=devoloper("shifna","finance",15000)
manager1=manager("fathima","hr",20000)

print("devoloper")
devoloper1.display()
print("salary:",devoloper1.calculate_salary())

print("manager")
manager1.display()
print("salary:",manager1.calculate_salary())





           
       
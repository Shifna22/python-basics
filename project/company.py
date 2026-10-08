# Create a Company class with a show_company() method. Create an Employee class
# that inherits from Company and has a show_employee() method. Create
# a Manager class that inherits from Employee and has a manage_team() method. Create
# a Manager object and call all three methods




class company:
    def show_company(self):
        print("companyname:",self.companyname)
class employee(company):
    def show_employee(self):
        print("name:",self.name)
        print("id:",self.id)
        print("dept:",self.dept)
        print("exp:",self.exp)
class manager(employee):
    def manage_team(self):
        print("team id:",self.teamid)
        print("nos:",self.nos)


managers=[]
n=int(input("enter no mangers:"))
for i in range(n):
    print("managers",i+1,"details")
manager1=manager()
manager1.companyname=input("enter company name:")
manager1.name=input("enter manager name:")
manager1.id=int(input("enter emp id:"))
manager1.exp=int(input("enter manager exp:"))
manager1.dept=input("enter dept name:")
manager1.teamid=int(input("enter teamid :"))
manager1.nos=int(input("enter team nos:"))
managers.append(manager1)

print("manager details")
for manager in managers:
    manager.show_company()
    manager.show_employee()
    manager.manage_team()
    print()


















        



  
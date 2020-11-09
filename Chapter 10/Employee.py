#Employee.py

#Start of Employee Class
class Employee:
    def __init__(self, name, id, dept, title):
        self.name = name
        self.id = id
        self.dept = dept
        self.title = title

    def show_employee(self): #A function to return the attributes of the Employee object it is called on
        return self.name, self.id, self.dept, self.title
#End of Employee class

#Create three Employee objects
employee1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
employee2 = Employee("Mark Jones", "39119", "IT", "Programmer")
employee3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

employee_list = [employee1, employee2, employee3]

for each in employee_list: #Show the attributes for each Employee object
    print(each.show_employee())

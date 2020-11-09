#main.py

#Adding dependencies
import pickle
import Employee
from Employee import Employee
import os.path
from os import path

#A function to check if the user wants to quit
def check_quit(check_this):
    global quit
    if check_this.strip().lower() == "quit":
        print("\n\n/////WARNING////// Quitting will save the current list!")
        ays = input("\nAre you sure? (y/n):")
        if ays.strip().lower() == "y":
            quit = True
            print('\n\nStopping the program. . .')

#A function to search through the employee list
def search_employee():
    global employee_dict
    id_input = input("\nSearch an employee by their ID number: ")
    check_quit(id_input)
    if quit != True:
        employee = employee_dict[id_input] #The Employee object the user will be working with based on the ID they enter
        print(employee.name, "has the ID", employee.id, "and is listed as a(n)", employee.title, "in the", employee.dept, "department.")

#A function to add an employee to the employee list
def add_employee():
    global employee_dict
    name_input = input("\nWhat is the employee's name?: ")
    check_quit(name_input)
    if quit != True:
        id_input = input("\nWhat is the employee's ID?: ")
        check_quit(id_input)
        if quit != True:
            dept_input = input("\nWhat is the employee's department?: ")
            check_quit(dept_input)
            if quit != True:
                title_input = input("\nWhat is the employee's job title?: ")
                check_quit(title_input)
                if quit != True:
                    new_employee = Employee(name_input, id_input, dept_input, title_input) #Create a new Employee object with the attributes the user provided
                    key = new_employee.id #The key will be the id of this Employee object
                    employee_dict[key] = new_employee #The value pair to the key will be the entire new Employee object
                    print("The new list is now:")
                    for each in employee_dict:
                        print(employee_dict[each].show_employee())

#A function to modify an employee in the employee list
def change_employee():
    global employee_dict
    user_change = input("\nWho would you like to change? (ID number): ")
    check_quit(user_change)
    if quit != True:
        employee = employee_dict[user_change] #The Employee object the user will be working with based on the ID they enter
        print("\nYou will be changing", employee.name)
        custom_menu = """
    -----What would you like to change?-----
    Employee name /{}/ - name
    Employee department /{}/ - dept
    Employee title /{}/ - title
        """.format(employee.name, employee.dept, employee.title)
        print(custom_menu)
        option = input("\nSelect an option from the menu above: ")
        check_quit(option)
        if quit != True: #Whatever attribute the user wants to change will be changed in the employee object
            if option.strip().lower() == "name":
                new_name = input("\nWhat is the new name?: ")
                employee.name = new_name.strip().title()
                print("\nThe employee's new name is {}".format(employee.name))
            elif option.strip().lower() == "dept":
                new_dept = input("\nWhat is the new department?: ")
                employee.dept = new_dept.strip().title()
                print("\nThe employee's new name is {}".format(employee.dept))
            elif option.strip().lower() == "title":
                new_title = input("\nWhat is the new job title?: ")
                employee.title = new_title.strip().title()
                print("\nThe employee's new name is {}".format(employee.title))

#A funtion to delete an employee in the employee list
def delete_employee():
    global employee_dict
    user_delete = input("\nWhich employee would you like to remove? (ID number): ")
    check_quit(user_delete)
    if quit != True:
        employee = employee_dict[user_delete] #The Employee object the user will be working with based on the ID they enter
        print(employee)
        print("\nYou will be removing", employee.name)
        confirm_message = "\nAre you sure you want to delete " + employee.name + "? (y/n): "
        confirm_delete = input(confirm_message) #Make sure the user is positive they want to delete this employee
        check_quit(confirm_delete)
        if quit != True and confirm_delete.strip().lower() == "y": #If the user doesn't quit and they confirm the deletion then delete the employee
            del employee_dict[user_delete]
            print("\nThe new list is now:")
            for each in employee_dict:
                print(employee_dict[each].show_employee())

#Stating global variables
employee_dict = {}
quit = False

#Main funtion
def main():
    global employee_dict
    if path.exists("employees.pickle"): #Check if there is a pickle file and use it as the dictionary if it exists
        with open("employees.pickle", "rb") as infile:
            employee_dict = pickle.load(infile)

        print("The current list is:") #Show the user the list of employees they are working with
        for each in employee_dict:
            print(employee_dict[each].show_employee())

    while quit != True: #As long as the user doesn't want to quit keep running the program
        print("""
        ----------What would you like to do?----------
        Search for an employee - search
        Add a new employee - add
        Change an employee's name, department, or job title - change
        Delete an employee from the dictionary - delete
        Quit at any time - quit
        """)
        user_choice = input("Type a keyword to do something!: ")
        check_quit(user_choice)

        if user_choice.strip().lower() == "search":
            search_employee()

        elif user_choice.strip().lower() == "add":
            add_employee()

        elif user_choice.strip().lower() == "change":
            change_employee()

        elif user_choice.strip().lower() == "delete":
            delete_employee()

    with open("employees.pickle", "wb") as outfile: #After the loop is finished running save the current employee dictionary to a file
        pickle.dump(employee_dict, outfile)

#Call the main function
main()

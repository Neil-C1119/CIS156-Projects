#11exercise1.py

#Start Employee class
class Employee:
    def __init__(self, name, number):
        self.__name = name

        if type(number) is int:
            self.__number = int(number)
        else:
            raise Exception("Please enter a number for the employee number")

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        if type(number) is int:
            self.__number = number
        else:
            raise Exception("Please enter a number for the employee number")

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number
#End Employee class

#Start ProductionWorker class (subclass/child of Employee class)
class ProdutionWorker(Employee):
    def __init__(self, name, number, shift, pay):
        Employee.__init__(self, name, number) #Initialize with Employee as the superclass/parent

        if int(shift) == 1 or int(shift) == 2: #Check if the input is either a 1 or 2
            self.__shift = int(shift)
        else:
            raise Exception("Shift number should be 1 or 2")

        if type(pay) is int or type(pay) is float: #Check if the input can be converted to a floating point
            self.__pay = float(pay)
        else:
            raise Exception("Please enter a number for the pay")

    def set_shift(self, shift):
        if shift == 1 or shift == 2: #Check if the input is either a 1 or 2
            self.__shift = shift
        else:
            raise Exception("Shift number should be 1 or 2")

    def set_pay(self, pay): #Check if the input is either an integer or floating point
        if type(pay) is int or type(pay) is float:
            self.__pay = pay
        else:
            raise Exception("Please enter a number for the pay")

    def get_shift(self):
        return self.__shift

    def get_pay(self):
        return self.__pay
#End ProductionWorker class

#Main function
def main():
    name_input = input("\nWhat is the worker's name?: ")

    try: #If the input cannot be converted to an integer throw an exception
        number_input = int(input("\nWhat is the worker's number?: "))
    except ValueError:
        print("The worker's number should be an integer")

    try: #If the input cannot be converted to an integer throw an exception
        shift_input = int(input("\nWhat is the worker's shift number?: "))
    except ValueError:
        print("The shift number should be 1 or 2")

    try: #If the input cannot be converted to a floating point throw an exception
        pay_input = float(input("\nWhat is the worker's hourly pay rate?: "))
    except ValueError:
        print("The worker's pay should be an integer or decimal")

    worker = ProdutionWorker(name_input, number_input, shift_input, pay_input)

    print("\n\nName- {}; Number- {}; Shift- {}; Hourly Pay- ${}".format(worker.get_name().title(), worker.get_number(), worker.get_shift(), worker.get_pay())) #Print the worker's information
    input("\nPress enter to terminate. . .")

main()

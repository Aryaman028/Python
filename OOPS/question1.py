class Employee:
    
    def __init__(self) :
        pass

    # def set_employee_id(self,id):
    #     self.employee_id = id

    # def set_employee_name(self,name):
    #     self.employee_name = name

    # def set_employee_id(self,work):
    #     self.employee_work = work

    def set_employee_data(self,id,name,work):
        self.employee_id = id
        self.employee_name = name
        self.employee_work = work
    def get_id(self):
        return self.employee_id
    def get_name(self):
        return self.employee_name
    def get_work(self):
        return self.employee_work


print("Welcome to our office new client")
print("You have to submit your details first")
id = int(input("Enter your ID number-->"))
name = input("Enter your name-->")
work = input("Enter your Work Shift-->")


my_employee_information = Employee()
my_employee_information.set_employee_data(id,name,work)
print("Your data has been uploaded succesfully")
print()
print(my_employee_information.get_id())
print(my_employee_information.get_name())
print(my_employee_information.get_work())





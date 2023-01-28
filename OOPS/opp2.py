class computer:
    no_of_leaves= 4
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.role=arole
        self.salary=asalary
    # these are called constructors
    def config(self):
        print("hello world")
    def printnumber(self):
        print("Vande Mataram",self.name,self.salary,self.role)
    def change_leaves(cls):
        cls.no_of_leaves = 10
    def from_str(cls,string):
        params = string.split("-")
        print(params)
        return cls(params[0],params[1],params[2])

# comp1 = computer("Raghav",50,"leader")  #instance
# if argument is given to the class then we have to use init function to grab the arguments
# comp2 = computer("Aryaman",50000,"manager")
# comp2 = computer()
# comp1 =computer()
# comp1.name="Raghav"
# comp2.name="Aryaman"
# comp2.salary=50000
# comp2.role="manager"
karan =computer.from_str("karan-480-student")
print(karan.salary)
# comp1.config()
# comp1.name="aryaman"

# print(comp1.__dict__)
# comp1.printnumber()
# print(comp1.name)
# print(comp2.name)
# print(comp1.name)
# print(comp2.salary)
# print(comp2.role)
# comp2.config()
# comp2.printnumber()
# comp1.change_leaves()
# print(comp1.no_of_leaves)

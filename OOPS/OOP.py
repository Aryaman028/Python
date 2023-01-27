# object -- instance
# classes --  design, blueprint
# polymmorphism
# abstraction
# encapsulation

# class Computer: 
class computer:
    def config(self):
        print("hello world")
comp1 = computer()  #instance
# comp1.config()
comp1.name="aryaman"
comp1.roll= 51
comp1.std= 13
comp1.sec = "A"
print(comp1.__dict__)
# it will return a dictionary having all instance variable
# we cant change the class variable from instance variable
# but we can chnage the instance varibale
print(computer.__dict__)

# print(comp1.name)


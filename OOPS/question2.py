class Car:
    def __init__(self):
        pass
    def get_details(self,car):
        self.car_name = car
        if car == "Prius":
            self.car_price = "30LAKH"
            self.yearofmake = 2014
            
        if car == "Camry":
            self.car_price = "50lakh"
            self.yearofmake = 2015

        if car == "Highlander":
            self.car_price = "60lakh"
            self.yearofmake = 2020
    def show_details(self):
        print("You selected this car", self.car_name)
        print("Price of this car is ", self.car_price)
        print("Year of make of this car is ", self.yearofmake)
    def __str__(self):
        print("YOu choosed this car", self.car_name)

def main():
    print("<--Welcome to TOYOTA showroom-->")
    print("We are currently having these cars")
    print("1.Prius")
    print("2.Camry")
    print("3.Highlander")
    c = input("Input car name for details as given in the list")
    data = Car()
    data.get_details(c)
    print("Your car data is here-->")
    data.show_details()
    
main()









            
            
            
            
            




    
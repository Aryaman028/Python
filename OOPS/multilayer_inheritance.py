class electronic_device:
    works_on = "battery"
    def printthis(self):
        return f"Yes this works on {self.works_on}"
    
class pocket_device(electronic_device):
    works_on = "cell"
    def printthis(self):
        return f"Yes this works on {self.works_on}"
    
class phone(pocket_device):
    pass
    # works_on = "lithium"
    # def printthis(self):
        # return f"Yes this works on {self.works_on}"
vivo = phone()
mobile = electronic_device()
cell_phone = pocket_device()
print(mobile.printthis())
print(vivo.printthis())


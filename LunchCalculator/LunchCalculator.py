from nicegui import ui


salesTax = 0.08375
gratuity = 0
complete = ["done","finish", ""]

class CalculationVariables:
    def __init__(self, name, item, price):
        self.name = name
        self.item = item
        self.price = price
        self.tax = price*salesTax
        self.tip = price*gratuity
        self.totalPrice = self.price + self.tax + self.tip
        
    def fullprice(self):
        return '{}: ${}'.format(self.name, self.totalPrice)

def modifyGratuity():
    changedGratuity = input("How much is the tip? ")
    gratuity = changedGratuity
    return gratuity

def addNames():
    while checker not in complete:
        checker = input("Enter Name: ")
        CalculationVariables.name = checker
        
def addItemName():
    itemName = input("what's the name of the item?")
    CalculationVariables.item = itemName
    
def addItemPrice():
    itemPrice = input("What is the price of the item?")
    CalculationVariables.price = itemPrice
    
    
    




def main():
    addNames()
    
if __name__ == "__main__":
    main()
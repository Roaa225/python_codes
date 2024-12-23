class Customer:
    
    def __init__(self, name, balance=5):  
        self.name = name
        self.balance = balance
        print("The init method was called")
        
    def __str__(self):
        return 'Customer: ' + str(self.name) + ', balance: ' + str(self.balance)
    
    def __eq__(self, other):
        return self.balance == other.balance


customer1 = Customer("roaa", 10)
customer2 = Customer("basma", 7)
print(str(customer1))
print(customer1 == customer2)


        

 
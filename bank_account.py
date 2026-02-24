class BankAccount:
    def __init__(self, name, blance, pin):
        self.name = name
        self.blance = blance
        self.__pin = pin

    def withdraw(self, amount, pin):
        if self.__check_pin(pin):      # calling private method
            if amount > self.blance:
                print("Insufficient balance")
            elif amount >= 20000:
                print("Maximum Aonunt is 20,000 Taka") 
            elif amount % 5000 != 0:
                print("You can withdraw only 500 & 1000 notes")
            else:
                self.blance -= amount
                print(f"Withdraw successful blance {self.blance}")
        else:
            print("Wrong password")

    def __check_pin(self,pin):     # Privet method
        if self.__pin == pin:
            return True
        else:
            return False
        
    def check_blance(self, pin):      # check_balance method
        if self.__check_pin(pin):
            print(f"Available Blance: {self.blance}")
        else:
            print("Wrong Password")

    def deposit(self, amonunt):
        self.blance += amonunt
        print(f"Deposit successful Blacnce: {self.blance}")
        

# Example run    
b1 = BankAccount("Tuhin", 50000, 4625)   # Account Holder
b1.deposit(10000)      # Deposit 10,000 taka
b1.withdraw(3000, 4625) # Valid (multiple of 500) 

b1.check_blance(4625)  # use pin

b1.withdraw(3232, 4625) # Invalid 3232 taka
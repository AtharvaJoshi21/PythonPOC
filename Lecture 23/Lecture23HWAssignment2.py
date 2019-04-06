# WAP to implement bank account class which supports Deposit and Withdraw methods.
#   -[Hint] Auto generate account number, by taking one class attribute

class BankAccount:
    accountNumber = 1
    minAccountBalance = 1000
    def __init__(self, initialBalance):
        self.__balance = initialBalance
    
    def __del__(self):
        del self.__balance

    def __repr__(self):
        return "Current Account Balance is {}".format(self.__balance)
    
    def Deposit(self, amount):
        self.__balance += amount
        return True
    
    def Withdraw(self, amount):
        if (self.__balance - amount) < self.minAccountBalance:
            return False
        else:
            self.__balance -= amount
            return True

def DisplayMenu(bankAcc):
    ch = 1
    while ch > 0:
        print("1. Display Current Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        ch = eval(input("Please enter your choice: "))
        if ch == 1:
            print(bankAcc)
        
        elif ch == 2:
            amount = eval(input("Please enter amount to be withdrawn: "))
            result = bankAcc.Withdraw(amount)
            if result:
                print("Transaction Successful! Updated balance is: ")
                print(bankAcc)
            else:
                print("Transaction declined as minimum account balance will not be maintained")
        
        elif ch == 3:
            amount = eval(input("Please enter amount to be deposited: "))
            bankAcc.Deposit(amount)
            print("Current balance is: ")
            print(bankAcc)
        
        elif ch == 4:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice!")
            continue

def main():
    initialAmount = eval(input("Please enter amount to be added as initial amount: "))
    bankAcc = BankAccount(initialAmount)
    DisplayMenu(bankAcc)

if __name__ == "__main__":
    main()
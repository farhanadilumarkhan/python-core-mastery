class Account:
    def __init__(self , name , initial_balance):
        self.holder_name = name
        self.balance = initial_balance
        print(f"Acount created for {self.holder_name} with balance: {self.balance}")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def deposit(self , amount):
        self.balance = self.balance + amount
        print(f"{amount} amount deposit total balance: {self.balance}")

    def withdraw(self , amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"{amount} successfully withdraw remaining balance: {self.balance}")
        else:
            print("Insufficient balance")

accounts_db = {}

while True:
    print("------ Banking System ------")
    print("1. Create New Acount")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter your choice (1 - 4): ")

    if choice == '1':
        name = input("Enter your name: ")
        initial_balance = int(input("Enter Initial balance amount: "))
        new_acc = Account(name , initial_balance)
        accounts_db[name] = new_acc
        print(f"Acount for {name} saved in database successfully")

    elif choice == '2':
        name = input("Enter your account name: ")
        if name in accounts_db:
            user_obj = accounts_db[name]
            user_obj.check_balance()
        else:
            print(f"Error! {name} account does not exist!")

    elif choice == '3':
        name = input("Enter account name: ")
        if name in accounts_db:
            user_obj = accounts_db[name]
            amt = int(input("Enter amount to deposit: "))
            user_obj.deposit(amt)
        else:
            print(f"Error {name} account does not exist!")
    
    elif choice == '4':
        name = input("ENter account name: ")
        if name in accounts_db:
            user_obj = accounts_db[name]
            amt = int(input("Enter amount to withdraw: "))
            user_obj.withdraw(amt)
        else:
            print(f"Error {name} acount does not exist!")

    elif choice == '5':
        print("Thank you for using our bank")
        break

    else:
        print("Invalid choice! please select (1 - 4)")
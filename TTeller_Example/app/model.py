import json

class InsufficientFundsError(Exception):
    pass

class Account:
    filepath = "data.json"
    
    def __init__(self, username):
        self.username = username
        self.pin = None
        self.balance = 0.0
        self.data = {}
        self.load()

    def load(self):
        try:
            with open(self.filepath) as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            pass
        
        if self.username in self.data:
            self.balance = self.data[self.username]["balance"]
            self.pin = self.data[self.username]["pin"]
    
    def save(self):
        self.data[self.username] = {
            "balance": self.balance,
            "pin": self.pin
        }
        with open(self.filepath, "w") as json_file:
            json.dump(self.data, json_file) 
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        if self.balance < amount:
            raise InsufficientFundsError
        self.balance -= amount
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        self.balance += amount
    
    @classmethod
    def login(cls, username, pin):
        account = cls(username)
        if pin != account.pin:
            return None
        else:
            return account
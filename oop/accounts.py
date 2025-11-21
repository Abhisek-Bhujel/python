import datetime
import pytz

class Account:
    """Simple account class with balance"""
    
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self._balance = balance
        self.transaction_list = []
        self.transaction_list.append((Account._current_time(), self._balance))
    
        print(f'An account was created for {self.name} with initial balance of ${self._balance:,.2f}')
    
    def deposit(self, amount: float) -> None:
        if amount <=  0:
            print('Deposit amount must to be greater than 0')
            return
        self._balance += amount
        print(f'Deposit of amount ${amount:,.2f} was successful')
        self.show_balance()
        self.transaction_list.append((Account._current_time(),amount))
    
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print('Withdrawal amount has to be greater than 0')
        elif amount > self._balance:
            print('Insufficient fund')
        else:
            self._balance -= amount
            print(f'Withdrawal of amount ${amount:,.2f} was successful')
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))
            
    
    def show_balance(self)->None:
        print(f'Your balance is {self._balance}')
        
    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))
    

if __name__ == '__main__':
    abhi = Account('Abhisek', 500)
    abhi.deposit(1000)
    abhi.withdraw(100)
    abhi.show_transactions()
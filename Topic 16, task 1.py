class CashRegister:
    def __init__(self, initial_amount=0):
        """Initialize the cash register with an optional initial amount"""
        self.balance = initial_amount
    
    def top_up(self, amount):
        """Add money to the cash register"""
        if amount < 0:
            raise ValueError("Amount to add must be positive")
        self.balance += amount
    
    def count_1000(self):
        """Return how many full thousands are left in the cash register"""
        return self.balance // 1000
    
    def take_away(self, amount):
        """Remove money from the cash register"""
        if amount < 0:
            raise ValueError("Amount to take must be positive")
        if amount > self.balance:
            raise ValueError("Not enough money in the cash register")
        self.balance -= amount
        return amount

# Example usage:
register = CashRegister(5000)  # Initialize with 5000

register.top_up(3000)         # Add 3000
print(register.balance)       # Output: 8000

thousands = register.count_1000()
print(f"Full thousands left: {thousands}")  # Output: Full thousands left: 8

try:
    register.take_away(6000)  # Take 6000
    print(f"New balance: {register.balance}")  # Output: New balance: 2000
    register.take_away(3000)  # This will raise an error
except ValueError as e:
    print(f"Error: {e}")      # Output: Error: Not enough money in the cash register
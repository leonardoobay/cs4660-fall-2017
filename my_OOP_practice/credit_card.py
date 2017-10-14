"""
Page 73 

Data Structures and Algorithms in Python

Goodrich

The self Identifier
In Python, the self identifier plays a key role. In the context of the CreditCard
class, there can presumably be many different CreditCard instances, and each must
maintain its own balance, its own credit limit, and so on. Therefore, each instance
stores its own instance variables to reflect its current state.
Syntactically, self identifies the instance upon which a method is invoked. For
example, assume that a user of our class has a variable, my card, that identifies
an instance of the CreditCard class. When the user calls my card.get balance( ),
identifier self, within the definition of the get balance method, refers to the card
known as my card by the caller. The expression, self. balance refers to an instance
variable, named balance, stored as part of that particular credit card’s state.




"""

class CreditCard:
"""A consumer credit card.”””

def init (self, customer, bank, acnt, limit):
"""Create a new credit card instance.

The initial balance is zero.

customer the name of the customer (e.g., John Bowman )
bank the name of the bank (e.g., California Savings )
acnt the acount identifier (e.g., 5391 0375 9387 5309 )
limit credit limit (measured in dollars)
"""
self. customer = customer
self. bank = bank
self. account = acnt
self. limit = limit
self. balance = 0

def get customer(self):
”””Return name of the customer.”””
return self. customer

def get bank(self):
”””Return the bank s name.”””
return self. bank

def get account(self):
”””Return the card identifying number (typically stored as a string).”””
return self. account

def get limit(self):
”””Return current credit limit.”””
return self. limit

def get balance(self):
”””Return current balance.”””
return self. balance


def charge(self, price):
”””Charge given price to the card, assuming sufficient credit limit.

Return True if charge was processed; False if charge was denied.
”””
if price + self. balance > self. limit: # if charge would exceed limit,
return False # cannot accept charge
else:
self. balance += price
return True

def make payment(self, amount):
”””Process customer payment that reduces balance.”””
self. balance −= amount



##############################Test
if name == __main__ :
wallet = [ ]
wallet.append(CreditCard( John Bowman , California Savings ,
5391 0375 9387 5309 , 2500) )
wallet.append(CreditCard( John Bowman , California Federal ,
3485 0399 3395 1954 , 3500) )
wallet.append(CreditCard( John Bowman , California Finance ,
5391 0375 9387 5309 , 5000) )

for val in range(1, 17):
wallet[0].charge(val)
wallet[1].charge(2 val)
wallet[2].charge(3 val)

for c in range(3):
print( Customer = , wallet[c].get customer( ))
print( Bank = , wallet[c].get bank())
print( Account = , wallet[c].get account( ))
print( Limit = , wallet[c].get limit( ))
print( Balance = , wallet[c].get balance())
while wallet[c].get balance( ) > 100:
wallet[c].make payment(100)
print( New balance = , wallet[c].get balance())
print( )

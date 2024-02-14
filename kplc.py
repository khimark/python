
from electricity import calculate_bill

#Bill calculator
customer_ID = int(input("Enter your ID: "))
customer_name = input("Enter your Name: ")
units_consumed = int(input("Enter units: "))

# Get the number of units consumed by the user
def kplc(customer_ID, customer_name, units):
  bill = calculate_bill(units)
  if units <=199:
    bill = units * 1.20
  elif units >= 200 and units < 400:
    bill = units * 1.50
  elif units >= 400 and units < 600:
    bill = units * 1.80
  elif units >= 600:
    bill = units * 2.00
    return bill
    
# Add a surcharge if the bill exceeds 400 shillings
  if bill > 400:
    bill += bill * 0.15
    
# Ensure minimum bill of 100 shillings
  if bill < 100:
    bill = 100
    return bill

print(kplc(customer_ID, customer_name, units_consumed))

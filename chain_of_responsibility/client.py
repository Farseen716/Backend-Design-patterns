"""An ATM Dispenser that dispenses denominations of notes"""

import sys
from atm_dispenser_chain import ATMDispenserChain

atm = ATMDispenserChain()
amount = int(input("Enter the amount to withdrawal : "))
if amount < 10 or amount % 10 != 0:
    print("Amount should be positive and in multiples of 10")
    sys.exit()

# Process the request
atm.chain1.handle(amount)
print("Now go spoil yourself")

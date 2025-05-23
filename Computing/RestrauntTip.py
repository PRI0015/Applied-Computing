bill=100
people = int(input("How many people would you like to split the bill with?"))
tip_percent = float(input("How much of a tip would you like to give? (%) "))
mile_cost = int(input("How many miles did the taxi travel?")) * 0.45
tip_amount = bill + tip_percent
tip_cost = bill + tip_amount
total = tip_cost + mile_cost
per_person = total / people
print("your total is", total, "dollars each person should pay", per_person, "dollars.")
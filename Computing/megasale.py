
amount_spent = float(input("Enter the amount spent: $"))
if amount_spent > 20:
    print("Customer is awarded a $3 voucher.")
elif amount_spent > 10:
    print("Customer is awarded a $1 voucher.")
else:
    print("requirements for a voucher not met.")

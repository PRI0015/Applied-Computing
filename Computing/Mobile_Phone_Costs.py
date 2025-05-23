pictures = int(input("How many pictures do you send per month?"))
texts = int(input("How many texts do you send per month?"))
data = float(input("How much data(MB) do you use per month?"))
cost = (pictures*0.35) + (texts*0.10) + (data*0.05)
print("Your total monthly bill is",f"${cost}",)
if cost > 10:
    print("You should get a contract.")
    
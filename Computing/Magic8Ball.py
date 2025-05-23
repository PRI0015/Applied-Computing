import random

answer1=("Absolutely!")
answer2=("No way Pedro!")
answer3=("Go for it tiger.")
print("Welcome to the Magic 8 Ball game—use it to answer your questions...")
question = input("Ask me for any advice and I’ll help you out. Type in your question and then press Enter for an answer")
print("shaking.... \n" * 4)
choice = random.randint(1,3)
if choice == 1:
    answer=answer1
elif choice == 2:
    answer=answer2
else:
    answer=answer3
print(answer)

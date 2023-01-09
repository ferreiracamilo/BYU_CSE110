#Core reqs
#Stretch 1 and %50 of Stretch 2

from statistics import mean 

account_name = ""
account_balance = 0
account_names = []
account_balances = []
max_account = ""
max_balance = 0

while account_name.lower() != "quit":
    account_name = input("What is the name of this account? ")
    if account_name.lower() == "quit":
        break #Accoring screenshot program stops immediately
    account_balance = float(input("What is the balance? "))
    account_names.append(account_name)
    account_balances.append(account_balance)

print("\nAccount Information:")
for i in range(len(account_balances)):
    print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")
    if max_balance < account_balances[i]:
        max_balance = account_balances[i]
        max_account = account_names[i]

print(f"\nTotal: ${sum(account_balances):.2f}")
print(f"Average: ${mean(account_balances):.2f}")
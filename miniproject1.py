print("=====Student Monthly Budget Analyzer=====")

name = input("Enter your name: ")
monthly_income = float(input("Enter your monthly income: "))
food = float(input("Enter the amount of money spent on food: "))
travel = float(input("Enter spendings on travel: "))
stdy = float(input("Enter spendings on study materials: "))
internet = float(input("Enter spendings on internet services: "))
others = float(input("Enter other expenses: "))

total = food + travel + stdy + internet + others 
balance_remaining = monthly_income - total 



if total != 0 :
    saving_rate = ( balance_remaining / total ) * 100

print("----- MONTHLY BUDGET REPORT -----")
print("\n Student: ",name)
print("Monthly income: ",monthly_income)
print("Food: ",food)
print("Travel: ",travel)
print("Study materials: ",stdy)
print("Mobile/Internet: ",internet)
print("Other: ",others)
print("\nTotal expenses: ",total)
print("Remaining balance: ",balance_remaining)
print(f"Savings rate : {saving_rate:.2f} %")

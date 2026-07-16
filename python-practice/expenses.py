name = input("Enter your name: (Sarah) ")
monthly_income = input("Enter your monthly income: (3000) ")
rent_expense = input("Enter your rent expense: (1200) ")
food_expense = input("Enter your food expense: (500) ")
transport_expense = input("Enter your transport expense: (300) ")

total_expenses = int(rent_expense or 1200) + int(food_expense or 500) + int(transport_expense or 300)
print(f"{name or 'Sarah'}, your total expenses are {total_expenses} and your remaining income is {int(monthly_income or 3000) - total_expenses}")
hours_worked = input("Enter hours worked: (40) ")
hourly_rate = input("Enter hourly rate: (15) ")

weekly_salary = int(hours_worked or 40) * int(hourly_rate or 15)
print(f"Weekly Salary: {weekly_salary}")
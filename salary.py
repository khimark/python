#enter salary and years_of_service
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

#give conditions
if years_of_service > 10:
  bonus = 0.1 * salary
  net_salary = salary + bonus
  print("Bonus: ", bonus)
  print("Net Salary: ", net_salary)
elif years_of_service >= 6 and years_of_service <= 10:
  bonus = 0.08 * salary
  net_salary = salary + bonus
  print("Bonus: ", bonus)
  print("Net Salary: ", net_salary)
elif years_of_service < 6:
  bonus = 0.05 * salary
  net_salary = salary + bonus
  print("Bonus: ", bonus)
  print("Net Salary: ", net_salary)

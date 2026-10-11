salary = 10000 # integer (số nguyên)
salary_coefficient = 4.0816 # float (số thực)
full_name = "Bai Yu" # character / string

print("-" * 50)

# ==============================================================================================
# 1. Format Symbol 1 (C-style)
# ==============================================================================================

strTT1 = "Full name: " + full_name + "\nSalary: " + str(salary)
print(strTT1)
# Full name: Bai Yu
# Salary: 10000

strTT2 = "Full name: %s \nSalary: %i \nSalary coefficient: %f"%(full_name, salary, salary_coefficient)
print(strTT2)
# Full name: Bai Yu
# Salary: 10000
# Salary coefficient: 4.081600

strTT3 = "Full name: %s \nSalary: %i \nSalary coefficient: %.2f"%(full_name, salary, salary_coefficient)
print(strTT3)
# Full name: Bai Yu
# Salary: 10000
# Salary coefficient: 4.08

# ==============================================================================================
# 2. Format Symbol 2 (new style)
# ==============================================================================================

str1 = f'Full name: {full_name}\nSalary: {salary}\nSalary coefficient: {salary_coefficient}'
print(str1)
# Full name: Bai Yu
#  Salary: 10000
#  Salary coefficient: 4.0816

# Add comma "," as a thousand separator for salary, and round the salary_coefficient up to 2 decimal numbers
str2 = f'Full name: {full_name}\nSalary: {salary:,} CNY\nSalary coefficient: {salary_coefficient:.2f}'
print(str2)
# Full name: Bai Yu
#  Salary: 10,000 CNY   
#  Salary coefficient: 4.08

# Add comma "," as a thousand separator for salary, and round the salary up to 2 decimal numbers
str3 = f'Full name: {full_name}\nSalary: {salary:,.2f} CNY\nSalary coefficient: {salary_coefficient}'
print(str3)
# Full name: Bai Yu
#  Salary: 10,000.00 CNY
#  Salary coefficient: 4.0816

# Use ``.ne`` for scientific notation
str4 = f'Full name: {full_name}\nSalary: {salary:.2e} CNY\nSalary coefficient: {salary_coefficient:.2e}'
print(str4)
# Full name: Bai Yu
#  Salary: 1.00e+04 CNY
#  Salary coefficient: 4.08e+00

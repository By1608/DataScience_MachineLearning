# Variable definition

# When you define a variable in Python, you must avoid using Python keywords
# Python keywords: https://www.w3schools.com/python/python_ref_keywords.asp

salary = 10000 # integer (số nguyên)
salary_coefficient = 4.0816 # float (số thực, dấu phẩy động)
single = True # kiểu luận lý boolean (True/False)
full_name = "Bai Yu" # character / string
job = 'Actor'

##-----------------------------------------------------##

company_info ='''
Company Yixin Entertainment
Location: 416 Beijing
'''

print(company_info)
# Company Yixin Entertainment
# Location: 416 Beijing

##-----------------------------------------------------##

# Multiple-variable definition
x, y, z = 3, 7, 15
print(x, y, z)

# ==============================================================================================
# GLOBAL VARIABLES vs LOCAL VARIABLES
# ==============================================================================================

student_name = 'Zhu Yilong' # Global variable, always exists after being defined, independent from For and While loops, or Function

def display_information_2():
    last_name = 'Zhu'
    first_name = 'Siyu'
    print(f'2 - Student name (local variable): {first_name} {last_name}')

def display_information_3():
    global last_name2 # Define last_name2 as global. Using this way, although the variable is defined inside a function, it is still a global variable
    last_name2 = 'Zhu ' # hence, it still persists after the execution of the function

    global first_name2
    first_name2 = 'Siyu'

# ==============================================================================================
# function calls and outputs
# ==============================================================================================

display_information_1()

display_information_2()
print(f'Student name (global): {student_name}') # The global variable student_name still persists

display_information_3()
print(f'3 - Student name (Global): {first_name2} {last_name2}')  # The global variables first_name2 and last_name2 still persist

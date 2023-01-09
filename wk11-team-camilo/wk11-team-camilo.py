import os

### GLOBAL VARIABLES ###
list_employees = []
### GLOBAL VARIABLES ###

### LOAD FILE BEFORE ASKING INPUT - DONE JUST ONCE ###
dir_path = os.path.dirname(os.path.realpath(__file__)) #retrieve root folder for py file
file_name = "hr_system.txt"
final_path = ""

#REVIEW THE DIR PATH TO DECIDE WHAT CHAIN CHARS or CHAR TO PLACE so can be executed on different operative systems
if dir_path.find("/") != -1:
    final_path = dir_path + "/" + file_name
elif dir_path.find("//") != -1:
    final_path = dir_path + "//" + file_name
elif dir_path.find("\\") != -1:
    final_path = dir_path + "\\" + file_name

with open(final_path) as data_file:
    for line in data_file:
        line = line.strip().split(" ") #It is splitted as well doing the strip to remove unwanted/unexpeted blank spaces
        #It is easier to save each employee as a list within the general employees list, it will be stored as
        #Name,ID,Title,AnnualSalary
        one_employee = [line[0],int(line[1]),line[2],float(line[3])] #ID is casted into int and salary into float
        list_employees.append(one_employee)

print()
print("1 - Get the name and the job title for each person")
print("2 - Display values following format: 'name (ID: id_number), job_title - $salary (annual salary)'")
print("3 - Calculate paycheck if employees are paid twice a month -engineers are eligible for a bonus of $1000-")
input_option = int(input("Select option from above -input number-: "))

if input_option == 1:
    for employee in list_employees:
        print(f"Name: {employee[0]}, Title: {employee[2]}")
elif input_option == 2:
    for employee in list_employees:
        print(f"{employee[0]} (ID: {employee[1]}), {employee[2]} - ${employee[3]:.2f} (annual salary)")
elif input_option == 3:
    for employee in list_employees:
        bimonthly_salary = employee[3]/24
        if employee[2] == "Engineer":
            bimonthly_salary += 1000
        print(f"{employee[0]} (ID: {employee[1]}), {employee[2]} - ${bimonthly_salary:.2f}")
else:
    print("You have not selected a valid option, it was a pleasure helping you")
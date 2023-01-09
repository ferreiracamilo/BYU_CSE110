from statistics import mean 

input_number = 100
numbers = []

while input_number != 0:
    input_number = int(input("Enter your number to append, if zero will stop: "))
    if input_number != 0:
        numbers.append(input_number)

print(f"The sum is: {sum(numbers)}")
# This would be a definition of average based on sum and quantity of elements, otherwise import mean function
# print(sum(numbers)/len(numbers))
print(f"The average is: {mean(numbers):.3f}")
print(f"The largest number is: {max(numbers)}")
#Smallest positive number
print(f"The smallest number is: {min([n for n in numbers if n>0])}")

#a blank line at the start
print("\nFind below the sorted list of numbers given by user")
for number in sorted(numbers):
    print(number)
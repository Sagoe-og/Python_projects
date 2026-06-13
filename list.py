#creating the list
numbers = []

print("Enter a list of numbers... Type 0 when finished")
while True:
    new_number = int(input("Enter number: "))
    if new_number == 0:
        break
    numbers.append(new_number)

#printing out the values of the list while also calculating for the largest value in the list
largest = numbers[0] if numbers else 0
print("The numbers are:")
for number in numbers:
    if number > largest:
        largest = number
    print(f" {number}")

#printing out the total values
total = sum(numbers)
print(f"The sum is: {total}")

#finding and printing out the average value
average = total / len(numbers) if numbers else 0
print(f"The average is: {average}")

#displaying the largest value in the list
print(f"The largest number is: {largest}")

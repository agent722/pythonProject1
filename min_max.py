num_of_integers = int(input("How many integers would you like to enter?"))
while num_of_integers <= 0:
    print("you must enter at least one positive integer")
    num_of_integers = int(input("How many integers would you like to enter?"))

count = 1

print("Please enter", num_of_integers, "integers.")
user_input = int(input())
min = user_input
max = user_input

while count <= num_of_integers -1:
    user_input = int(input())
    if user_input >= max:
        max = user_input
    if user_input < max and user_input < min:
        min = user_input
    count += +1

print("Min: ",min)
print("Max: ",max)



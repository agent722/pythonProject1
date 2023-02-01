user_input = int(input("Please enter a positive integer."))
while user_input < 1:
    print("Please enter a positive integer")
    user_input = int(input("Please enter a positive integer."))
print("The factors of",user_input,"are:")
for U_Inputs in range(1, user_input + 1):
    if user_input % U_Inputs == 0:
        print(U_Inputs)

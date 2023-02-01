# Author: Christopher Burckhardt
# GitHub username: agent722
# Date: 1/30/2023
# Description: This program will find the term in the fibinocci sequnce and give the solution.

def fib(term):

    """This function will find a number in a sequence at the term they choose. The function uses a for loop to
    take the sum of two numbers and add the sum to the previous number
    in the sequence. For example: 3+5=8 then 5+8=13 then 8+13 =21 and so on."""

    first = 1
    second = 0
    for i in range(0, term):
        third = first + second
        first = second
        second = third
    return third


user_input = int(input("term = fib()"))
#print(fib(user_input))
#test2
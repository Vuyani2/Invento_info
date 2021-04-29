#declaring a function with one parameter
number_1 = 15
#allocate the number
def fact(number_1):
    #function return one when parameter is 1 or 0
    if number_1 == 1 or number_1 == 0:
        return 1
    else:
        #function call itself
        return number_1 * fact(number_1 - 1)
#call function
print(fact(number_1))
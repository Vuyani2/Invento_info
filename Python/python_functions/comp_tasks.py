marks3={'Andy':"asdfghb", "Amy":"qrtyga", "Billy":"afzxcv"}
appearences = 0
for sd in marks3:
    appearences += 1

print(appearences)

#def Numbers_To_Words (number):
    #number=str(number)
 #   result = ''
  #  dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero"}
    # loop through number

   # return " ".join(map(lambda x: dict[x], str(number)))
#print(Numbers_To_Words(1234))


#       check each character in number dict.get(1)
#       result = result + " " + dict.get(1)
# 123 = one two three

def number_function(numbers):
    result = ''
    numbers = str(numbers)
    numbers_list = ['zero', 'one', 'two', 'three', "four", "five", "six", "seven", "eight", "nine"]

    for each_number in numbers:
        #print(numbers_list[int(each_number)])
        result = result + " " + numbers_list[int(each_number)]

        #print(result)
    print(result)


number_function(6781)


def check_appear(letter, word):
    appearance = 0

    for each_letter in word:
        if each_letter == letter:
            appearance = appearance + 1

    return appearance

print(check_appear('e', 'everywhere'))
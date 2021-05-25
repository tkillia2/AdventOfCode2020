# Explanation of today's goal provided here: https://adventofcode.com/2020/day/2

# Will be reading a file with lines formatted like shown below
# 11-16 z: kfslzzwszdmsnptcz
# 5-6 g: qgggggk

# the numbers are the range of the following letter that must be present in
# the password that follows
import re
words = open('passwords.txt')


total = 0
valid = 0
for pw in words:
    # Reset a counts dictionary for each word to get the total number of each
    # letter in the password string
    counts = {}

    # use a regex to get the minimum amount of times the letter can appear
    minNum = re.findall('[0-9]*-', pw)[0]
    minNum = int(minNum.strip('-'))
    
    # same as minNum but for the maximum amount of times it can appear
    maxNum = re.findall('-[0-9]* ', pw)[0]
    maxNum = maxNum.strip(' ')
    maxNum = int(maxNum.replace('-', ''))

    # Use a regex to get the number to being looking for
    Letter = re.findall('[a-z]:', pw)[0]
    Letter = Letter.strip(':')
    
    # Regex to separate the password from the rest of the string
    password = re.findall(': [a-z]*', pw)[0]
    password = password.strip(': ')

    # At times the desired letter never appears so set to 0 beforehand to
    # avoid errors
    counts[Letter] = 0

    # now working through the password to create the dictionary
    for letter in password:
        # if the letter has never appeared it was 0 and then add 1 otherwise
        # just add 1
        counts[letter] = counts.get(letter, 0) + 1
    # Now if the appearences by the letter fit within the specified range add
    # one to the total variable
    if counts[Letter] >= minNum and counts[Letter] <= maxNum:
        total += 1


    # Now for part 2: using min and max numbers as locations where one and
    # only one must  be the desired letter to be valid
    ## First off must take one off for max and min numbers to fit python 
    # rules with the Advent of Code rules
    minNum = minNum-1
    maxNum = maxNum-1

    # Now just check and add to valid variable
    if(password[minNum] == Letter and password[maxNum] != Letter):
        valid += 1
    if(password[minNum] != Letter and password[maxNum] == Letter):
        valid += 1

print(f'The total number of passwords that fit part 1: {total}')
print(f'The total number of passwords that fit part 2: {valid}')

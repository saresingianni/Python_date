'''
Martin A. Aaberge
supplement code for Meduim Article:
"How You Make Sure input() is the Type You Want it to Be – in Python"

'''


def is_digit(check_input):
    '''
    function checking if your string is a pure digit, int
    return : bool
    '''
    if check_input.isdigit():
        return True
    return False

def is_string_only(check_input):
    '''
    function checking if your string is all letters
    return : bool
    '''    
    if check_input.isalpha():
        return True
    return False

def is_string_with_space(check_input):
    '''
    function checking if your string is all letters, but including space(s)
    return : bool
    '''   
    valid = False
    if ' ' in check_input:
        for char in check_input:
            if char.isdigit():
                valid = False
            elif char.isalpha() or char.isspace():
                valid = True
    return valid

def is_string_or_num(check_input):
    '''
    function checking if your string is all letters or numbers
    return : bool
    '''       
    if check_input.isalnum():
        return True
    return False

def is_float(check_input):
    '''
    function checking if your string is a floating point
    return : bool
    '''   
    if '.' in check_input:
        split_number = check_input.split('.')
        if len(split_number) == 2 and split_number[0].isdigit() and split_number[1].isdigit():
                return True
    return False


'''
food list example. 
We have a food list and want the user to select an item based on the 
index of that item
'''

food_list = ['milk' , 'bread' , 'cheese']

#menu:
print (f'Item Choices:')
for index, item in enumerate(food_list):
    print(f'{index} : {item}')
print (f'type \'exit\' to exit the program\n')

#set user input to nothing to force entry into the while loop
user_input = ''
while user_input != 'q':
    user_input = input('pick your item from the list above: ')

    #make sure the user types an actual integer if the input is not q (to quit)
    while user_input != 'q' and not is_digit(user_input):
        print (f'please try again, integer is required as input')
        user_input = input('pick your item from the list above: ')

    #if the user does not want to quit, we will print the choice
    if user_input != 'q':
        print (f'You chose {food_list[int(user_input)]}')

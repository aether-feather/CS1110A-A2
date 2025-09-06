# Family Dictionary by Rahael Joseph

# Functions make the program more readable and important parts of your code reusable; you must define them before the main block of your program
# This function creates and returns a list that stores the birthdate and address to represent each member
def member(birthdate, address):
    member = [birthdate, address]
    return member

print('Family Dictionary by Rahael Joseph \n') # Title

# Empty dictionary to fill with the user's entries
family_dict = {

} 

while True:
    # Asks the user what they want to do from the list of options
    operation = int(input('> Add a family member (1) \n> Remove a family member (2) \n> Exit (3) \n>> ')) 
    print()

    # Adding a family member
    if operation == 1: 
        name = input('Name: ')
        birthdate = input('Birthdate (Month Day, Year): ')
        address = input('Address: ')

        # Spacing for readability (either \n or an empty print() statement)
        print() 

        # Calls the earlier member() function to create the list and add it to the 'family_dict' dictionary
        family_dict[name] = member(birthdate, address) 

        print(f'Current family dictionary:\n {family_dict}\n')

     # Removing a family member
    if operation == 2:
        # 'not' is a boolean that checks if the dictionary 'family_dict' is empty (returns true if empty, false if not empty)
        if not family_dict: 
            print('No entries to remove.\n')
        else:
            # Asks for the member to be removed and removes their entry from 'family_dict'
            name_to_remove = input('Name: ')
            del family_dict[name_to_remove]
            print()
            if not family_dict:
                print('Current family dictionary is now empty.\n')
            else:
                print(f'Current family dictionary:\n {family_dict}\n')         

    # Breaks the loop
    if operation == 3:
        break
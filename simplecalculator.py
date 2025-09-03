# Simple Calculator by Rahael Joseph in Visual Studio Code

# Every number entered is converted to a float for ease of calculation.

# Note: A while-true loop executes the code nested underneath forever until the value of True changes
# or the 'break' command is used
while True:
    # Asks the user for the operation (or if they want to exit)
    operation = input('Addition, Subtraction, Multiplication, Division, or Exit (case sensitive)? ')

    # Addition
    if operation == 'Addition':
        x = float(input('Enter the first rational number: '))
        y = float(input('Enter the second rational number: '))

        print(f'{x} + {y} = {x + y:.3f} \n')
    # Subtraction
    # Note: Elif stands for else-if, a statement that runs if the conditions of the previous if-statement
    # were not fulfilled and the conditions of the elif statement itself were fulfilled
    elif operation == 'Subtraction':
        x = float(input('Enter the first rational number: '))
        y = float(input('Enter the second rational number: '))

        print(f'{x} - {y} = {x - y:.3f} \n')
    # Multiplication
    elif operation == 'Multiplication':
        x = float(input('Enter the first rational number: '))
        y = float(input('Enter the second rational number: '))

        print(f'{x} * {y} = {x * y:.3f} \n')
    # Division, does not accept y = 0
    elif operation == 'Division':
        x = float(input('Enter the first rational number: '))
        y = float(input('Enter the second rational number: '))

        while y == 0:
            y = float(input('Cannot divide by zero. Try again: '))

        print(f'{x} / {y} = {x / y:.3f} \n')
    # Ends the loop (and program)
    elif operation == 'Exit':
        print('Thanks for stopping by :> \n')

        break


parentheses.py: 
    parentheses_checker:
    - checks if the parentheses in the expression are valid
    - creates a stack to keep track of the parentheses
    - if the stack is empty at the end of the expression, returns "yes"
    - otherwise, returns "no"

calculator.py:
    addition:
    - adds two numbers
    - returns the result

    multiplication:
    - multiplies two numbers
    - returns the result

    exponentiation:
    - raises a number to the power of another number
    - returns the result

    calculator:
    - takes in three parameters: number1, operation, number2
    - uses the operation to determine which function to call
    - returns the result

    operationChecker:
    - takes in three parameters: operation, expressionList
    - checks if the operation is valid
    - if the operation is valid, it performs the operation
        - it takes the left and right values and performs the operation
        - it replaces the operation and the two values with the result
        - it removes the two values from the expression list
        - it returns the new expression list
    - if the operation is not valid, it returns -1

    parse_expression:
    - takes in an expression
    - parses the expression into a list of tokens
    - for each character in the expression:
        - if the character is a digit or a decimal point, it adds it to the current number
        - if the character is an operator or parentheses, it adds it to the expression list
            - it also checks if the last character in the expression list is an operator
                - if it is, it returns -1
        - if the character is a space, it skips it
        - if the character is not a digit, a decimal point, an operator, or a space, it returns -1
    - it returns the expression list

    solve_parentheses:
    - takes in an expression list
    - it creates a result list
    - it iterates through the expression list
    - if the current character is a '(', it pushes it onto the stack
    - if the current character is a ')', it pops the stack until it finds a '('
    - if the current character is an operator, it pops the stack until it finds an operator with lower precedence
    - it pushes the current operator onto the stack
    - if the current character is a number, it adds it to the result list
    - it returns the result list

    main:
    - takes in an expression
    - it parses the expression
    - it solves the parentheses
    - it calculates the expression
    - it prints the result 

Logic Flow:
    - to start the program, run the command "python calculator.py <input_string>"
    - the program starts by checking if the input string is empty
    - if it is not empty, it will parse the expression through parse_expression
    - if it is empty, it will print "The input string is empty."
    - if the expression is valid, it will solve the parentheses through solve_parentheses
    - if the expression is not valid, it will print "Error in expression"
    - if the expression is valid, it will calculate the expression through calculator
    - if the expression is not valid, it will print "Error in expression"
    - it will print the result to command line
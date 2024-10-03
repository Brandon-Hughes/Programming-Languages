The code starts at the main execution, which is the entry point of the program. It parses the expression through using the grammar.lark file to build a parse tree, then transforms the parse tree into an abstract syntax tree (AST) using the CalcTransformer class. Finally, it evaluates the AST into a result through the evaluate function and prints the result as a decimal number. 

Every function broken down: 
    main execution:
        - define a parser calc_transformer from CalcTransformer()
        - get input string from command line arguments
        - parse the input string into a parse tree using the grammar.lark file
        - transform the parse tree into an abstract syntax tree (AST) using calc_transformer
        - evaluate the new AST into a result throught the evaluate function
        - print the result as a decimal number

    CalcTransformer:
        - define a method paren that takes a list of items and returns a tuple with the first item and the rest of the items
        - define a method exponent that takes a list of items and returns a tuple with the first item and the rest of the items
        - define a method log that takes a list of items and returns a tuple with the first item and the rest of the items
        - define a method times that takes a list of items and returns a tuple with the first item and the rest of the items
        - define a method plus that takes a list of items and returns a tuple with the first item and the rest of the items
        - define a method neg that takes a list of items and returns a tuple with the first item and the rest of the items
        - define a method minus that takes a list of items and returns a tuple with the first item and the rest of the items
        - define a method num that takes a list of items and returns a tuple with the first item and the rest of the items
        
    evaluate:
        - if the input is a log, recursively evaluate the first item and the second item
        - if the input is a plus, recursively evaluate the first item and the second item
        - if the input is a times, recursively evaluate the first item and the second item
        - if the input is a neg, recursively evaluate the first item
        - if the input is a minus, recursively evaluate the first item and the second item
        - if the input is a paren, recursively evaluate the first item
        - if the input is a exponent, recursively evaluate the first item and the second item
        - if the input is a num, return the first item
        - otherwise, raise a ValueError


import sys
sys.path.append('../Assignment1') 
from parentheses import parentheses_checker

def addition(a, b):
    return int(a)+int(b)

def multiplcation(a, b):
    return int(a)*int(b)

def exponentiation(a, b):
    return int(a)**int(b)


def calculator(number1, operation, number2):
    if(operation == "+"):
        return addition(number1, number2)
    elif(operation == "*"):
        return multiplcation(number1, number2)
    elif(operation == "^"):
        return exponentiation(number1, number2)
    else:
        print("That is not a valid operation")

def operationChecker(operation, expressionList):
    currPos = 0
    while currPos < len(expressionList):
        if expressionList[currPos] == operation:
            if currPos > 0 and currPos + 1 < len(expressionList):
                left = expressionList[currPos-1]
                right = expressionList[currPos+1]
                result = calculator(left, operation, right)
                expressionList[currPos-1] = result
                expressionList.pop(currPos+1)
                expressionList.pop(currPos)
                currPos = 0
            else:
                return [-1]
        else:
            currPos += 1
    return expressionList

def parse_expression(expression):
    expression_list = []
    current_number = ""
    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        elif char in "+*^()":
            if current_number:
                expression_list.append(current_number)
                current_number = ""
            if char in "()":
                expression_list.append(char)
            else:
                if len(expression_list) > 0 and expression_list[-1] not in "()":
                    if expression_list[-1] in "+*^":
                        return -1
                expression_list.append(char)
        elif char == " ":
            continue
        else:
            return -1
    if current_number:
        expression_list.append(current_number)
    return expression_list

def solve_parentheses(expression_list):
    result = []
    i = 0
    while i < len(expression_list):
        if expression_list[i] == '(':
            paren_count = 1
            j = i + 1
            while j < len(expression_list) and paren_count > 0:
                if expression_list[j] == '(':
                    paren_count += 1
                elif expression_list[j] == ')':
                    paren_count -= 1
                j += 1
            
            if paren_count != 0:
                return -1
            
            inner_result = solve_parentheses(expression_list[i+1:j-1])
            if inner_result == -1:
                return -1
            
            inner_result = operationChecker("^", inner_result)
            inner_result = operationChecker("*", inner_result)
            inner_result = operationChecker("+", inner_result)
            
            if len(inner_result) != 1:
                return -1
            
            result.append(str(inner_result[0]))
            i = j
        else:
            result.append(expression_list[i])
            i += 1
    
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculator.py \"<input_string>\"")
        sys.exit(1)
        
    input_string = sys.argv[1]
    if (len(input_string) == 0):
        print("The input string is empty.")
    else:
        expression = parse_expression(input_string)
        if expression == -1:
            print("Error in expression")
        else:
            parentheses = parentheses_checker(input_string)
            if parentheses == "yes":
                solved_expression = solve_parentheses(expression)
                if solved_expression == -1:
                    print("Error in expression")
                else:
                    result = operationChecker("^", solved_expression)
                    result = operationChecker("*", result)
                    result = operationChecker("+", result)
                    if len(result) == 1:
                        print(result[0])
                    else:
                        print("Error: Invalid expression")
            else:
                print("The parentheses are not balanced.")


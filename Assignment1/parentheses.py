import sys

def parentheses_checker(expression):
    count = 0
    for char in expression:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:
            return "no"
    if count == 0:
        return "yes"
    else:
        return "no"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parentheses.py \"<input_string>\"")
        sys.exit(1)

    input_string = sys.argv[1]

    result = parentheses_checker(input_string)
    print(result)


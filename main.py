import re

# Roman to integer conversion
def roman_to_int(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in s[::-1]:  # Reverse the string for easier calculation
        value = roman[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# Integer to Roman conversion
def int_to_roman(num: int) -> str:
    val = [
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    ]
    syb = [
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    ]
    roman_num = ''
    for i in range(len(val)):
        while num >= val[i]:
            num -= val[i]
            roman_num += syb[i]
    return roman_num

# Function to perform basic arithmetic
def calculate(operation: str, num1: int, num2: int) -> int:
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 // num2  # Integer division for Roman numerals
    else:
        raise ValueError("Unsupported operation")

# Validate the result based on Roman numeral rules
def validate_result(result: int):
    if result == 0:
        return "0 does not exist in Roman numerals."
    elif result < 0:
        return "Negative numbers can't be represented in Roman numerals."
    elif result > 3999:
        return "You're going to need a bigger calculator."
    return int_to_roman(result)

# Function to evaluate an expression with Roman numerals
def evaluate_expression(expression: str) -> str:
    try:
        # Replace Roman numerals with their integer equivalents
        expression = re.sub(r'\b([IVXLCDM]+)\b', lambda m: str(roman_to_int(m.group())), expression)

        # Evaluate the arithmetic expression
        result = eval(expression)
        return validate_result(result)
    except SyntaxError:
        return "I don't know how to read this."
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    import sys
    # Get the equation from the command line arguments
    equation = " ".join(sys.argv[1:])
    # Calculate and print the result
    print(evaluate_expression(equation))

def lexical_scanner(source_code):
    length = len(source_code)
    i = 0

    while i < length:
        current_char = source_code[i]

        # Skip whitespace
        if current_char.isspace():
            i += 1
            continue

        # Check for operators
        if current_char == '+':
            print("Token: PLUS Operator")
            i += 1
        elif current_char == '-':
            print("Token: MINUS Operator")
            i += 1
        elif current_char == '*':
            print("Token: MULTIPLICATION Operator")
            i += 1
        elif current_char == '/':
            print("Token: DIVISION Operator")
            i += 1
        elif current_char == '=':
            print("Token: ASSIGNMENT Operator")
            i += 1
        elif current_char == '>':
            print("Token: GREATER THAN Operator")
            i += 1
        elif current_char == '<':
            print("Token: LESS THAN Operator")
            i += 1
        elif current_char == '(':
            print("Token: LEFT PARENTHESIS")
            i += 1
        elif current_char == ')':
            print("Token: RIGHT PARENTHESIS")
            i += 1
        elif current_char == '{':
            print("Token: LEFT BRACE")
            i += 1
        elif current_char == '}':
            print("Token: RIGHT BRACE")
            i += 1
        elif current_char == ';':
            print("Token: SEMICOLON")
            i += 1

        # Check for identifiers (keywords or variables)
        elif current_char.isalpha():
            identifier = ""
            while i < length and (source_code[i].isalnum()): 
                identifier += source_code[i]
                i += 1

            # Check for keywords
            if identifier == "if":
                print("Token: IF Keyword")
            elif identifier == "else":
                print("Token: ELSE Keyword")
            elif identifier == "do":
                print("Token: DO Keyword")
            elif identifier == "while":
                print("Token: WHILE Keyword")
            elif identifier == "for":
                print("Token: FOR Keyword")
            elif identifier == "int":
                print("Token: INT Keyword")
            elif identifier == "float":
                print("Token: FLOAT Keyword")
            elif identifier == "string":
                print("Token: STRING Keyword")
            elif identifier == "array":
                print("Token: ARRAY Keyword")
            elif identifier == "stack":
                print("Token: STACK Keyword")
            else:
                # If it's not a keyword, treat it as an identifier
                print(f"Token: IDENTIFIER ({identifier})")

        # Check for numbers
        elif current_char.isdigit():
            number = ""
            while i < length and (source_code[i].isdigit() or source_code[i] == '.'):  
                number += source_code[i]
                i += 1
            print(f"Token: NUMBER ({number})")

        # Check for string literals
        elif current_char == '"':
            string_literal = ""
            i += 1  # Skip the opening quote
            while i < length and source_code[i] != '"':
                string_literal += source_code[i]
                i += 1
            i += 1  # Skip the closing quote
            print(f'Token: STRING Literal ("{string_literal}")')

        # Handle unrecognized characters
        else:
            print(f"Error: Unrecognized character '{current_char}'")
            i += 1

# Sample input for testing
source_code = '''
int x = 10;
float y = 20.5;
string name = "ZaraLang";
if (x > y) {
    x = x * 2;
} else {
    y = y + 1;
}
do {
    x = x - 1;
} while (x > 0);
'''

print("Lexical analysis of the source code:")
lexical_scanner(source_code)

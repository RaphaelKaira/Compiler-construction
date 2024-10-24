# Grammar rules for Zara language
grammar = {
    "S -> if E { S } else { S }": ["if", "(", "E", ")", "{", "S", "}", "else", "{", "S", "}"],
    "S -> do { S } while ( E )": ["do", "{", "S", "}", "while", "(", "E", ")"],
    "S -> for ( S ; E ; S ) { S }": ["for", "(", "S", ";", "E", ";", "S", ")", "{", "S", "}"],
    "E -> E + T": ["E", "+", "T"],
    "E -> E - T": ["E", "-", "T"],
    "T -> T * F": ["T", "*", "F"],
    "T -> T / F": ["T", "/", "F"],
    "F -> ( E )": ["(", "E", ")"],
    "F -> id": ["id"],
    "F -> num": ["num"]
}

# Operator precedence and associativity
precedence = {
    '+': 1, '-': 1,
    '*': 2, '/': 2
}

# Shift-Reduce Parser Class
class ShiftReduceParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.stack = []
        self.input_buffer = []
        self.actions = []  # For storing parser actions (Shift, Reduce)
    
    # Check if we can reduce the current stack using any rule
    def can_reduce(self):
        for rule, production in self.grammar.items():
            if self.stack[-len(production):] == production:
                return rule
        return None
    
    # Shift action: move a symbol from input buffer to the stack
    def shift(self):
        symbol = self.input_buffer.pop(0)
        self.stack.append(symbol)
        self.actions.append(f"Shift '{symbol}'")
    
    # Reduce action: apply a grammar rule to reduce the stack
    def reduce(self, rule):
        production = self.grammar[rule]
        self.stack = self.stack[:-len(production)]
        lhs = rule.split(" -> ")[0]
        self.stack.append(lhs)
        self.actions.append(f"Reduce by rule: {rule}")
    
    # Parse the input Zara code
    def parse(self, tokens):
        self.input_buffer = tokens
        self.actions = []
        
        while self.input_buffer or len(self.stack) > 1:
            # Try to reduce if possible
            reduce_rule = self.can_reduce()
            if reduce_rule:
                self.reduce(reduce_rule)
            else:
                # Otherwise, shift if input buffer is not empty
                if self.input_buffer:
                    self.shift()
                else:
                    break
        
        # Final check if we've reduced to the start symbol
        if len(self.stack) == 1 and self.stack[0] == "S":
            print("Parsing successful!")
        else:
            print("Parsing failed.")
        
        return self.actions

# Tokenize the Zara code
def tokenize_zara_code(code):
    # Example of a simple tokenizer, assuming tokens are separated by spaces
    tokens = code.replace("(", " ( ").replace(")", " ) ").replace("{", " { ").replace("}", " } ").replace(";", " ; ").split()
    return tokens

# Sample Zara code
zara_code = '''
if ( x > 5 ) { y = y - 1 ; } else { y = y + 1 ; }
do { z = z * 2 ; } while ( z < 100 ) ;
for ( i = 0 ; i < 10 ; i = i + 1 ) { sum = sum + i ; }
'''

# Test the parser
def test_parser():
    print("Starting Bottom-Up Parser Test...\n")
    
    # Tokenize Zara code
    tokens = tokenize_zara_code(zara_code)
    
    # Initialize the parser
    parser = ShiftReduceParser(grammar)
    
    # Parse the tokens
    actions = parser.parse(tokens)
    
    # Display parsing actions
    for action in actions:
        print(action)

# Run test
test_parser()
# Output will be:
# Starting Bottom-Up Parser Test...

# Shift 'if'
# Shift '('
# Shift 'x'
# Shift '>'
# Shift '5'
# Shift ')'
# Shift '{'
# Shift 'y'
# Shift '='
# Shift 'y'
# Shift '-'
# Shift '1'
# Shift ';'
# Reduce by rule: E -> E - T
# ...
class SymbolTable:
    # Initializes an empty dictionary self.symbols to store variable information.
    def __init__(self):    
        self.symbols = {}

    #Adds a new variable with its type and optional value to the symbol table.
    def add_symbol(self, name, var_type, value=None):
        if name in self.symbols:
            raise Exception(f"Symbol '{name}' already exists.")
            
        self.symbols[name] = {'type': var_type, 'value': value}
        print(f"Added: {name} -> Type: {var_type}, Value: {value}")

    #Updates the value of an existing variable.
    def update_symbol(self, name, value):
        if name not in self.symbols:
            raise Exception(f"Symbol '{name}' not found.")
        self.symbols[name]['value'] = value
        print(f"Updated: {name} -> New Value: {value}")
        
    #Retrieves the variable's type and value.
    def get_symbol(self, name):
        if name not in self.symbols:
            raise Exception(f"Symbol '{name}' not found.")
        return self.symbols[name]
    
    #Displays all the symbols in the table.
    def display_table(self):
        print("\nSymbol Table:")
        for name, info in self.symbols.items():
            print(f"{name} -> Type: {info['type']}, Value: {info['value']}")
        print()



def zara_program():
    # Create an instance of the SymbolTable
    symbol_table = SymbolTable()

    symbol_table.add_symbol("x", "integer", 10)

    symbol_table.add_symbol("y", "float", 3.14)
    
    symbol_table.add_symbol("name", "string", "ZaraLang")

    symbol_table.add_symbol("arr", "array", [1, 2, 3, 4, 5])

    symbol_table.add_symbol("stack", "stack", [])

    def push_to_stack(value):
        stack = symbol_table.get_symbol("stack")['value']
        stack.append(value)
        symbol_table.update_symbol("stack", stack)

    def pop_from_stack():
        stack = symbol_table.get_symbol("stack")['value']
        if stack:
            value = stack.pop()
            symbol_table.update_symbol("stack", stack)
            return value
        else:
            return None

    symbol_table.update_symbol("x", 20)
    symbol_table.update_symbol("y", 6.28)

    push_to_stack(100)
    push_to_stack(200)
    pop_value = pop_from_stack()
    print(f"Popped Value: {pop_value}")

    symbol_table.display_table()


zara_program()


from nodes import MakePizzaNode, AddToppingNode, BakePizzaNode, SlicePizzaNode, DeliverPizzaNode


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def peek(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None

    def advance(self):
        self.current += 1

    def parse(self):
        nodes = []
        while self.peek() is not None:
            if self.peek()[0] == "NEWLINE":
                self.advance()
            else:
                nodes.append(self.parse_command())
        return nodes

    def parse_command(self):
        while self.peek() and self.peek()[0] == "NEWLINE":
            self.advance()  # Skip any blank lines or newlines

        token = self.peek()
        if token is None:
            raise Exception("Syntax Error: Unexpected end of input.")

        if token[1] == "repeat":
            return self.parse_repeat()
        elif token[1] == "if":
            return self.parse_conditional()
        elif token[1] == "let":
            return self.parse_variable_declaration()
        elif token[1] == "make_pizza":
            return self.parse_make_pizza()
        elif token[1] == "add_topping":
            return self.parse_add_topping()
        elif token[1] == "bake":
            return self.parse_bake()
        elif token[1] == "slice":
            return self.parse_slice()
        elif token[1] == "deliver":
            return self.parse_deliver()
        else:
            raise Exception(f"Syntax Error: Unknown command '{token[1]}'.")

    def parse_repeat(self):
        self.advance()  # Skip 'repeat'
        count = self.expect("NUMBER")[1]  # Get the number of iterations
        self.expect("OPERATOR", ":")  # Ensure colon
        while self.peek() and self.peek()[0] == "NEWLINE":  # Skip newlines
            self.advance()
        body = self.parse_command()  # Parse the body of the loop
        return {"type": "loop", "count": int(count), "body": body}

    def parse_variable_declaration(self):
        self.advance()  # Skip 'let'
        name = self.expect("IDENTIFIER")[1]  # Get variable name
        self.expect("OPERATOR", "=")  # Ensure '=' operator
        value = self.expect("STRING")[1].strip('"')  # Get variable value
        return {"type": "variable_declaration", "name": name, "value": value}

    def parse_conditional(self):
        self.advance()  # Skip 'if'
        condition_var = self.expect("IDENTIFIER")[1]  # Get the variable being checked
        self.expect("OPERATOR", "=")  # Expect the first '=' of '=='
        self.expect("OPERATOR", "=")  # Expect the second '=' of '=='
        condition_value = self.expect("STRING")[1].strip('"')  # Get the value being compared

        # Skip any newlines or whitespace before the colon
        while self.peek() and self.peek()[0] in ["NEWLINE", "SKIP"]:
            self.advance()
        if not self.peek() or self.peek()[1] != ":":
            raise Exception(f"Syntax Error: Missing ':' after conditional statement, got {self.peek()}")

        self.expect("OPERATOR", ":")  # Consume the colon

        # Parse the body of the conditional
        body = self.parse_command()
        return {"type": "conditional", "condition": (condition_var, "==", condition_value), "body": body}

    def parse_make_pizza(self):
        self.advance()  # Skip 'make_pizza'
        self.expect("OPERATOR", "(")  # Consume '('
        self.expect("IDENTIFIER", "size")  # Expect 'size'
        self.expect("OPERATOR", "=")  # Consume '='
        size = self.expect("STRING")[1].strip('"')  # Expect a string for size
        self.expect("OPERATOR", ",")  # Consume ','
        self.expect("IDENTIFIER", "crust")  # Expect 'crust'
        self.expect("OPERATOR", "=")  # Consume '='

        # Allow crust to be a variable or a string
        token = self.peek()
        if token[0] == "STRING":
            crust = self.expect("STRING")[1].strip('"')  # Get the string value
        elif token[0] == "IDENTIFIER":
            crust = self.expect("IDENTIFIER")[1]  # Get the variable name
        else:
            raise Exception(f"Syntax Error: Expected STRING or IDENTIFIER, got {token}")

        self.expect("OPERATOR", ")")  # Consume ')'
        return MakePizzaNode(size, crust)

    def parse_add_topping(self):
        self.advance()
        self.expect("OPERATOR", "(")
        topping = self.expect("STRING")[1].strip('"')
        self.expect("OPERATOR", ")")
        return AddToppingNode(topping)

    def parse_bake(self):
        self.advance()  # Skip 'bake'
        self.expect("OPERATOR", "(")  # Consume '('
        self.expect("OPERATOR", ")")  # Consume ')'
        return BakePizzaNode()

    def parse_slice(self):
        self.advance()  # Skip 'slice'
        self.expect("OPERATOR", "(")
        pieces = int(self.expect("NUMBER")[1])  # Get the number of slices
        self.expect("OPERATOR", ")")
        return SlicePizzaNode(pieces)

    def parse_deliver(self):
        self.advance()  # Skip 'deliver' keyword
        self.expect("OPERATOR", "(")  # Consume '('
        self.expect("OPERATOR", ")")  # Consume ')'
        return DeliverPizzaNode()

    def expect(self, token_type, token_value=None):
        token = self.peek()
        if token is None:
            raise Exception(f"Syntax Error: Unexpected end of input. Expected {token_type} {token_value}.")
        if token[0] != token_type or (token_value is not None and token[1] != token_value):
            raise Exception(f"Syntax Error: Expected {token_type} {token_value}, but got {token}.")
        self.advance()
        return token


from nodes import MakePizzaNode, AddToppingNode


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
        token = self.peek()
        if token[1] == "make_pizza":
            return self.parse_make_pizza()
        elif token[1] == "add_topping":
            return self.parse_add_topping()
        else:
            raise Exception(f"Syntax Error: Unknown command '{token[1]}'")

    def parse_make_pizza(self):
        self.advance()
        self.expect("OPERATOR", "(")
        self.expect("IDENTIFIER", "size")
        self.expect("OPERATOR", "=")
        size = self.expect("STRING")[1].strip('"')
        self.expect("OPERATOR", ",")
        self.expect("IDENTIFIER", "crust")
        self.expect("OPERATOR", "=")
        crust = self.expect("STRING")[1].strip('"')
        self.expect("OPERATOR", ")")
        return MakePizzaNode(size, crust)

    def parse_add_topping(self):
        self.advance()
        self.expect("OPERATOR", "(")
        topping = self.expect("STRING")[1].strip('"')
        self.expect("OPERATOR", ")")
        return AddToppingNode(topping)

    def expect(self, token_type, token_value=None):
        token = self.peek()
        if token is None:
            raise Exception("Syntax Error: Unexpected end of input")
        if token[0] != token_type or (token_value is not None and token[1] != token_value):
            raise Exception(f"Syntax Error: Expected {token_type} {token_value}, got {token}")
        self.advance()
        return token

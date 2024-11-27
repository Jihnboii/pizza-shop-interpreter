from lexer import Lexer
from parser import Parser
from nodes import MakePizzaNode, AddToppingNode


# Evaluator Class
class Evaluator:
    def __init__(self):
        self.active_pizza = None

    def evaluate(self, ast_structure):
        for command_node in ast_structure:
            if isinstance(command_node, MakePizzaNode):
                self.make_pizza(command_node)
            elif isinstance(command_node, AddToppingNode):
                self.add_topping(command_node)

    def make_pizza(self, pizza_node):
        self.active_pizza = {"size": pizza_node.size, "crust": pizza_node.crust, "toppings": []}
        print(f"Making a {pizza_node.size} pizza with {pizza_node.crust} crust.")

    def add_topping(self, topping_node):
        if not self.active_pizza:
            raise Exception("Runtime Error: No pizza to add toppings to!")
        self.active_pizza["toppings"].append(topping_node.topping)
        print(f"Added topping: {topping_node.topping}")


if __name__ == "__main__":
    # Read the input program from a file
    with open("program.pza", "r") as file:
        pizza_program_code = file.read()

    lexer = Lexer(pizza_program_code)
    token_stream = lexer.tokenize()

    parser = Parser(token_stream)
    abstract_syntax = parser.parse()

    evaluator = Evaluator()
    evaluator.evaluate(abstract_syntax)

from lexer import Lexer
from parser import Parser
from nodes import MakePizzaNode, AddToppingNode, BakePizzaNode, SlicePizzaNode, DeliverPizzaNode
import os
import time

# Evaluator Class
class Evaluator:
    def __init__(self):
        self.active_pizza = None
        self.variables = {}  # Stores variable declarations
        self.valid_sizes = ["Small", "Medium", "Large"]
        self.valid_crusts = ["Thin", "Regular", "Thick"]
        self.valid_toppings = ["Pepperoni", "Cheese", "Mushrooms", "Olives", "Sausage", "Bacon", "Peppers", "Extra Cheese"]

    def evaluate(self, ast_structure):
        for command_node in ast_structure:
            try:
                if isinstance(command_node, MakePizzaNode):
                    self.make_pizza(command_node)
                elif isinstance(command_node, AddToppingNode):
                    self.add_topping(command_node)
                elif isinstance(command_node, BakePizzaNode):
                    self.bake_pizza()
                elif isinstance(command_node, SlicePizzaNode):
                    self.slice_pizza(command_node)
                elif isinstance(command_node, DeliverPizzaNode):
                    self.deliver_pizza()
                elif isinstance(command_node, dict):  # Handle new constructs
                    if command_node["type"] == "loop":
                        for _ in range(command_node["count"]):
                            self.evaluate([command_node["body"]])  # Evaluate loop body
                    elif command_node["type"] == "conditional":
                        condition, operator, value = command_node["condition"]
                        variable_value = self.variables.get(condition)
                        if operator == "==" and variable_value == value:
                            self.evaluate([command_node["body"]])  # Evaluate if condition is True
                    elif command_node["type"] == "variable_declaration":
                        self.variables[command_node["name"]] = command_node["value"]
                        print(f"Variable '{command_node['name']}' set to '{command_node['value']}'")
                    else:
                        raise Exception(f"Runtime Error: Unknown command type '{command_node['type']}'")
            except Exception as e:
                print(f"Error: {str(e)}")

    def make_pizza(self, pizza_node):
        size = pizza_node.size
        crust = self.variables.get(pizza_node.crust, pizza_node.crust)  # Resolve variable if necessary

        if size not in self.valid_sizes:
            raise Exception(f"Runtime Error: Invalid size '{size}'. Valid sizes are: {', '.join(self.valid_sizes)}")
        if crust not in self.valid_crusts:
            raise Exception(f"Runtime Error: Invalid crust '{crust}'. Valid crusts are: {', '.join(self.valid_crusts)}")

        self.active_pizza = {"size": size, "crust": crust, "toppings": []}
        print(f"Making a {size} pizza with {crust} crust.")

    def add_topping(self, topping_node):
        topping = topping_node.topping or self.get_user_input("Enter topping: ")

        if topping not in self.valid_toppings:
            raise Exception(
                f"Runtime Error: Invalid topping '{topping}'. Valid toppings are: {', '.join(self.valid_toppings)}")

        if not self.active_pizza:
            raise Exception("Runtime Error: No pizza to add toppings to!")

        self.active_pizza["toppings"].append(topping)
        print(f"Added topping: {topping}")

    def bake_pizza(self):
        if not self.active_pizza:
            raise Exception("Runtime Error: No pizza to bake!")
        print(f"Baking the pizza: {self.active_pizza['size']} with {self.active_pizza['crust']} crust.")

    def slice_pizza(self, slice_node):
        if not self.active_pizza:
            raise Exception("Runtime Error: No pizza to slice!")
        print(f"Slicing the pizza into {slice_node.pieces} pieces.")
        print("Pizza sliced successfully!")

    def deliver_pizza(self):
        if not self.active_pizza:
            raise Exception("Runtime Error: No pizza to deliver!")
        print(
            f"Delivering the pizza: {self.active_pizza['size']} with {self.active_pizza['crust']} crust and toppings: {', '.join(self.active_pizza['toppings'])}.")
        self.active_pizza = None  # Reset after delivery

    def get_user_input(self, prompt):
        value = input(prompt).strip()
        return value


if __name__ == "__main__":
    while True:
        import os

        # List available .pza files
        files = [f for f in os.listdir(".") if f.endswith(".pza")]
        if not files:
            print("No .pza files found in the current directory.")
            exit(1)

        print("Available .pza files:")
        for idx, file in enumerate(files):
            print(f"{idx + 1}: {file}")

        # Prompt the user to select a file
        choice = input("Enter the number of the .pza file to execute (or type 'exit' to quit): ").strip()
        if choice.lower() == 'exit':
            print("Exiting the interpreter. Goodbye!")
            break

        try:
            file_index = int(choice) - 1
            if 0 <= file_index < len(files):
                selected_file = files[file_index]
            else:
                print("Invalid selection.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Read the selected file
        with open(selected_file, "r") as file:
            pizza_program_code = file.read()

        lexer = Lexer(pizza_program_code)
        token_stream = lexer.tokenize()

        parser = Parser(token_stream)
        try:
            abstract_syntax = parser.parse()
        except Exception as e:
            print(f"Error during parsing: {str(e)}")
            continue  # Go back to menu for another file

        evaluator = Evaluator()
        evaluator.evaluate(abstract_syntax)
        # Add a pause before showing the menu again
        time.sleep(2)


# Pizza Shop Interpreter 🍕

This project is a custom interpreter for a pizza-themed programming language. It allows you to simulate a simple pizza ordering system by writing commands in a `.pza` file. The interpreter processes these commands to create and manage pizza orders.

---

## Features
- Create a pizza with a specific size and crust type.
- Add toppings to the pizza.
- Bake the pizza.
- Slice the pizza into pieces.
- Deliver the pizza with details about its size, crust, and toppings.
- Menu system to dynamically select `.pza` files to execute.
- Handles syntax and runtime errors gracefully.

---

## Requirements
- **Python 3.10+** (or a compatible version)
- Any text editor for creating `.pza` files (e.g., VSCode, Notepad++, or a simple text editor).

---

## Installation
1. Clone or download this repository to your local machine.
2. Ensure you have Python installed.
3. Navigate to the project folder.

---

## How to Use
1. Place your `.pza` files in the same directory as `interpreter.py`.
2. Run the interpreter:
    ```bash
    python interpreter.py
    ```
3. Select a `.pza` file from the menu to execute it.
4. After execution, the menu will reappear, allowing you to run another file or exit the interpreter.

### Example `.pza` File
```plaintext
let crust = "Thin"
make_pizza(size="Large", crust=crust)
add_topping("Cheese")
bake()
slice(8)
deliver()
```

---

## Example Output
For the above `.pza` file, the interpreter will output:
```plaintext
Variable 'crust' set to 'Thin'
Making a Large pizza with Thin crust.
Added topping: Cheese
Baking the pizza: Large with Thin crust.
Slicing the pizza into 8 pieces.
Pizza sliced successfully!
Delivering the pizza: Large with Thin crust and toppings: Cheese.
```

---

## Command Reference
### `let variable = "value"`
- Declares a variable that can be used in subsequent commands.
- Example: `let crust = "Thin"`

### `make_pizza(size="Size", crust="Crust")`
- Starts a new pizza with the given size and crust type.
- Example: `make_pizza(size="Large", crust="Thin")`

### `add_topping("Topping")`
- Adds a topping to the current pizza.
- Example: `add_topping("Cheese")`

### `bake()`
- Bakes the pizza. Must be done before slicing or delivering.

### `slice(Pieces)`
- Slices the pizza into the specified number of pieces.
- Example: `slice(8)`

### `deliver()`
- Delivers the pizza. Prints out the pizza's size, crust, and toppings.

---

## Error Handling
- **Syntax Errors**:
  - Clearly indicate issues such as missing values, unknown commands, or incomplete statements.
  - Example: `Syntax Error: Expected STRING, but got NEWLINE`.
- **Runtime Errors**:
  - Handle invalid inputs like unsupported sizes, crusts, or toppings gracefully.
  - Example: `Runtime Error: Invalid topping 'Pineapple'. Valid toppings are: Pepperoni, Cheese, Mushrooms, Olives, Sausage, Bacon, Peppers`.

---

## Future Enhancements
- Add support for multiple pizzas.
- Implement interactive mode.
- Expand commands to handle drinks, sides, and desserts.

---

## License
This project is open-source and available under the MIT License.

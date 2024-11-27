# Pizza Shop Interpreter 🍕

This project is a custom interpreter for a pizza-themed programming language. It allows you to simulate a simple pizza ordering system by writing commands in a `.pza` file. The interpreter processes these commands to create and manage pizza orders.

---

## Features
- Create a pizza with a specific size and crust type.
- Add toppings to the pizza.
- Bake the pizza.
- Slice the pizza into pieces.
- Deliver the pizza with details about its size, crust, and toppings.

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
1. Create a `.pza` file with your pizza commands. Example:
    ```plaintext
    make_pizza(size="Large", crust="Thin")
    add_topping("Cheese")
    bake()
    slice(8)
    deliver()
    ```
2. Run the interpreter:
    ```bash
    python interpreter.py
    ```
3. The program reads the `.pza` file and executes the commands in sequence.

---

## Example Output
For the `.pza` file:
```plaintext
make_pizza(size="Large", crust="Thin")
add_topping("Cheese")
bake()
slice(8)
deliver()
```

The interpreter will output:
```plaintext
Making a Large pizza with Thin crust.
Added topping: Cheese
Baking the pizza...
Slicing the pizza into 8 pieces.
Delivering the pizza: Large with Thin crust and toppings: Cheese.
```

---

## Command Reference
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

## Future Enhancements
- Add support for multiple pizzas.
- Implement interactive mode.
- Expand commands to handle drinks, sides, and desserts.

---

## License
This project is open-source and available under the MIT License.

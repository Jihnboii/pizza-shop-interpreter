class MakePizzaNode:
    def __init__(self, size, crust):
        self.size = size
        self.crust = crust

    def __repr__(self):
        return f"MakePizzaNode(size={self.size}, crust={self.crust})"


class AddToppingNode:
    def __init__(self, topping):
        self.topping = topping

    def __repr__(self):
        return f"AddToppingNode(topping={self.topping})"



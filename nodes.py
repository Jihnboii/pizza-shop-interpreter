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


class BakePizzaNode:
    def __repr__(self):
        return "BakePizzaNode()"


class SlicePizzaNode:
    def __init__(self, pieces):
        self.pieces = pieces

    def __repr__(self):
        return f"SlicePizzaNode(pieces={self.pieces})"


class DeliverPizzaNode:
    def __repr__(self):
        return "DeliverPizzaNode()"

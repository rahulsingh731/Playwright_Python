class multiplication_logic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiply_l(self):
        if not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float))):
            raise TypeError("Both a and b must be numbers")
        return self.a * self.b
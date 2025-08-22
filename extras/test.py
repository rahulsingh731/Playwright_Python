import test2


class OopsDemo():
    def __init__(self, a, b):
        # super().__init__(a, b)  # Call parent class's __init__ to set self.a and self.b
        self.a = a
        self.b = b

    def __init__(self,path):
        self.path = path

    def addition(self):
        if not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float))):
            raise TypeError("Both a and b must be numbers")
        return self.a + self.b

    # def multiply(self):
    #     return super().multiply_l()

    def read_file(self):
        file = open(self.path)
        return file



# obj = OopsDemo(10, 12)
obj = OopsDemo("abc.txt")
# print(obj.addition())
print(obj.read_file().readlines())

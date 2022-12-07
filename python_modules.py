class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b



def maths():
    print("Function of this module")


math = Math(10, 20)
print(math.sum())
maths()
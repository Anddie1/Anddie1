class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self): 
        print('Object is being deconstructered!')

    

person1 = Person('Adam', 17)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other): # there are also __Sub__ __div__ etc
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self): # how to represent a vector
        return f"X: {self.x}, Y: {self.x}"
    
v1 = Vector(10,20)
v2 = Vector(50,60)
v3 = v1 + v2

print(v3.x)
print(v3.y)
print(v3)
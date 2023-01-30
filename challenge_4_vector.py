import math
from functools import total_ordering

@total_ordering
class Vector:

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector: x axis: '{self.x}', y axis: '{self.y}', z axis: '{self.z}'"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Operation only support on instance of Vector class')

        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if not type(other) == int and not type(other) == float:
            raise TypeError('Operation only support on instance of Vector class')

        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        if not type(other) == int and not type(other) == float:
            raise TypeError('Operation only support on instance of Vector class')

        return self * other

    def __abs__(self):
        return math.sqrt(self.x **2 + self.y**2 + self.z **2)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __gt__(self, other):
        if not isinstance(other,Vector):
            return NotImplemented

        return abs(self) > abs(other)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __bool__(self):
        return bool(abs(self))

    def __getitem__(self, item):
        if type(item) == str and item.lower() in ['x', 'y','z']:
            return eval(f"self.{item.lower()}")

        else:
            return NotImplemented
v1 = Vector(1,2,3)
v2 = Vector(2,3,4)
print(v1['z'])



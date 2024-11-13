# vector2.py

from math import sqrt
from math import sqrt

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xy = (self.x, self.y)

    def __add__(self, other):
        # Addition of two 2-dimensional vectors
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Operands must be an instance of Vector2")
    
    def __sub__(self, other):
        # Subtraction of two 2-dimensional vectors
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Operands must be an instance of Vector2")
    
    def dotProduct(self, other):
        # Dot product of two 2-dimensional vectors (returns a scalar)
        if isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Operands must be an instance of Vector2")
        
    def crossProduct(self, other):
        # Returns the magnitude of the cross product in 2D (a scalar, as the z-component of the cross product)
        if isinstance(other, Vector2):
            return self.x * other.y - self.y * other.x
        else:
            raise TypeError("Operands must be an instance of Vector2")

    def multiplyByScalar(self, operand):
        # Multiplication of 2-dimensional vector by scalar operand
        if isinstance(operand, (int, float)):
            return Vector2(self.x * operand, self.y * operand)
        else:
            raise TypeError("Operand must be a number")

    def magnitude(self) -> float:
        # Returns the length of the 2-dimensional vector
        return sqrt(self.x**2 + self.y**2)

    def normalize(self):
        # Normalize 2-dimensional vector to a unit vector
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector2(self.x / magnitude, self.y / magnitude)

    def expandVector2ToVector3(self):
        # Returns a Vector3 representation (assuming Vector3 is defined elsewhere)
        return Vector3(self.x, self.y, 0)

    def __repr__(self):
        # Override of __repr__ to "Vector2(x, y)"
        return f"Vector2({self.x}, {self.y})"

    

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.xyz = (x, y, z)

    def __add__(self, other):
        # addition of 2 3-dimensional vectors
        if isinstance(self, type(other)):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Operands must be an instance of Vector3")
    
    def __subtract__(self, other):
        # subtraction of 2 3-dimensional vectors
        if isinstance(self, type(other)):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Operands must be an instance of Vector3")
    
    def dotProduct(self, other):
        # scalar multiplication of 2 3-dimensional vectors
        if isinstance(self, type(other)):
            return Vector2(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            raise TypeError("Operands must be an instance of Vector3")
        
    def crossProuct(self, other):
        # vector multiplication of 2 3-dimensional vectors
        if isinstance(self, type(other)):
            ax, ay, az = self.xyz
            bx, by, bz = other.xyz
            return Vector3(ay * bz - az * by,
                           az * bx - ax * bz,
                           ax * by - ay * bx)
        else:
            raise TypeError("Operands must be an instance of Vector3")

    def multyplyByScalar(self, operand):
        # multiplication vector by scalar operand
        if type(operand) == int:
            return Vector2(self.x * operand, self.y * operand, self.z * operand)
        else:
            raise TypeError("Operand must be a number")

    def magnitude(self) -> int:
        # magnitude of the vector
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def mormalize(self):
        # normalize 3-dimenzional vector to unit vector
        magnitude = self.magnitude
        return Vector2(self.x / self.magnitude, self.y / self.magnitude, self.z / self.magnitude)

    def shrinkVector3ToVector2(self):
        # returns Vector3
        if self.z == 0:
            return Vector2(self.x, self.y)
        else:
            return ValueError("Z factor of Vector 3 must be zero to be able to shrink it down")
    
    def __repr__(self):
        # override of __replr__ to "Vector3(x, y, z)"
        return f"Vector2({self.x}, {self.y}, {self.z})"

#vector add 메소드 생성

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
v3 = v1.add(v2)
print('v1.add(v2) =', v3)

#__add__ , __sub__ 특수 메소드
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
v3 = v1 + v2
print('v1 + v2) =', v3)
v4 = v1 - v2
print('v1 - v2 =', v4)


# 그 외의 특수 메소드
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    def __pow__(self, other):
        return Vector2D(self.x ** other.x, self.y ** other.y)
    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)
    def __floordiv__(self, other):
        return Vector2D(self.x // other.x, self.y // other.y)
    def __mod__(self, other):
        return Vector2D(self.x % other.x, self.y % other.y)
    def __pos__(self):
        return Vector2D(+self.x, +self.y)
    def __neg__(self):
        return Vector2D(-self.x , -self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)

v3 = v1 * v2
print('v1 * v2 =', v3)
v4 = v1 ** v2
v5 = v1 / v2
v6 = v1 // v2
v7 = v1 % v2
v8 = +v1
v9 = -v1
print(v4, v5,v6,v7,v8,v9)

#비교 연산자 특수 메소드

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __lt__(self,other):
        return Vector2D(self.x < other.x, self.y < other.y)
    def __le__(self, other):
        return Vector2D(self.x <= other.x, self.y <= other.y)
    def __ge__(self, other):
        return Vector2D(self.x >= other.x, self.y >= other.y)
    def __gt__(self, other):
        return Vector2D(self.x > other.x, self.y > other.y)
    def __eq__(self, other):
        return Vector2D(self.x == other.x, self.y == other.y)
    def __ne__(self, other):
        return Vector2D(self.x != other.x, self.y != other.y)
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)

v10 = v1<v2
v11 = v1<=v2
v12 = v1>=v2
v13 = v1>v2
v14 = v1==v2
v15 = v1!=v2

print(v10, v11, v12, v13, v14, v15)
    

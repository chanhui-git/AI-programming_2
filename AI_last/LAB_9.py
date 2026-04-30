#LAB 9-8 : 특수 메소드의 응용
#1,2
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self,other):
        return Vector2D(self.x * other.x, self.y * other.y)
    def __truediv__(self,other):
        return Vector2D(self.x / other.x, self.y / other.y)
    def __neg__(self):
        return Vector2D(-self.x, -self.y)
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector2D(30,40)
v2 = Vector2D(10,20)
v3 = v1 * v2
v4 = v1 / v2
v5 = -v2

print('v1 * v2 =', v3)
print('v1 / v2 =', v4)
print('-v1 =', v5)

#LAB 9-9 : 백터의 크기 비교하기
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x,self.y)
    def __gt__(self, other):
        return (self.x**2+self.y**2)**1/2 > (other.x**2+other.y**2)**1/2
    def __ge__(self, other):
        return (self.x**2+self.y**2)**1/2 >= (other.x**2+other.y**2)**1/2
    def __lt__(self, other):
        return (self.x**2+self.y**2)**1/2 < (other.x**2+other.y**2)**1/2
    def __le__(self, other):
        return (self.x**2+self.y**2)**1/2 <= (other.x**2+other.y**2)**1/2
    


v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
v3 = v1 > v2
v4 = v1 >= v2
v5 = v1 < v2
v6 = v1 <= v2
print('v1 > v2 =', v3)
print('v1 >= v2 =', v4)
print('v1 < v2 =', v5)
print('v1 <= v2 =', v6)

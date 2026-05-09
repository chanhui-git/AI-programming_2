#LAB 9-1 : 객체와 메소드 호출
#1
print((200).__sub__(100))
print((200).__mul__(100))
print((200).__truediv__(100))
#2
print([10,20,30,40].pop())
#3
#호출할 수 없는 메소드는 2) keys()
#4
print(dir(int))
#5
print(dir(list))

#LAB 9-2 : 용어 정리
#1
#a) 객체 지향 프로그래밍: 프로그램을 짤 때 프로그램을 실제 세상에 가깝게 모델링 하는 기법
#b) 절차적 프로그래밍: 함수나 모듈을 만들어두고 이것들을 문제해결 순서에 맞게 호출하여 수행하는 방식
#c) 그래픽 사용자 인터페이스: 사용자가 컴퓨터나 전자 기기와 상호작용할 때 그래픽 요소를 사용하여 시각적으로 조작할 수 있도록 돕는 환경

#2
#절차적 프로그래밍이 명령의 순차적인 실행에 집중한다면, 객체 지향 프로그래밍은 데이터와 기능을 '객체'라는 단위로 묶어 상호작용하게 함으로써 재사용성과 유지보수성을 높이는 방식입니다.

#LAB 9-3 : 용어 정리
#1
#a) 클래스: 객체를 만들어내기 위한 틀
#b) 객체: 클래스를 바탕으로 구현된 실체
#c) 인스턴스: 특정 클래스로부터 생성된 객체
#d) 클래스의 속성: 객체가 가지는 고유한 데이터
#e) 클래스의 동작: 객체가 수행할 수 있는 기능

#LAB 9-4 : Dog 클래스와 인스턴스 생성
class Dog:
    def bark(self):
        print('멍멍~~')
my_dog = Dog()
my_dog.bark()

#LAB 9-5 : Dog 클래스와 인스턴스 생성
class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        print('멍멍~~')
my_dog = Dog('Jindo')
my_dog.bark()

#LAB 9-6 : Dog 클래스와 문자열화 메소드
class Dog:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Dog(name = '+self.name+')'
my_dog = Dog('Jindo')
print('my_dog의 정보 :',my_dog)

#LAB 9-7 : 정수 객체의 is 연산
n = 100
m = 100
if n is m:
    print('n is m')
else:
    print('n is not m')

#n과 m이 같은 객체를 참조

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

#LAB 9-10 : __dict__를 이용한 인스턴스변수의 조회
#1
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
r1 = Rect(100,200)
print(r1.__dict__)
print(r1.__dict__['width'])

#2
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
r1 = Rect(100,200)
print(r1.__dict__)
print(r1.__dict__['_Rect__width'])

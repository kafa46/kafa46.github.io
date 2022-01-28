from abc import ABCMeta, abstractmethod

# 생명체 추상 클래스 - interface 형태로 코딩
class AbstractRemocon(metaclass=ABCMeta):
    
    def __init__(self, x, y, age):
        self.x = x
        self.y = y
        self.age = age
    
    # 일반 메서드: age
    def age(self,):
        self.age += 1
    
    # 일반 메서드: move
    def age(self, xDistance):
        self.x += xDistance
    
    def getX(self,):
        return self.x
    
    def setX(self, x):
        self.x = x
    
    def getY(self,):
        return self.y
    
    def setY(self, y):
        self.y = y
    
    
    
    # 추상 메서드 1
    @abstractmethod
    def television_on(self,):
        pass
    
    # 추상 메서드 2
    @abstractmethod
    def television_off(self,):
        pass
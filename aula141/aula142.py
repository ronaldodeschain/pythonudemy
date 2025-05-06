from abc import ABC,abstractmethod
#Foo - Bar são placeholders genericos para suas classes

class AbstractFoo(ABC):
    def __init__(self,name):
        self.name = name

    @property
    def name(self): ...

    @name.setter
    def name(self,name): ...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print('alalaOoo')

foo = Foo('Bar')
print(foo.name)
    

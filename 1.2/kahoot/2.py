from abc import abstractmethod, ABCMeta

class MyBaseClass(metaclass=ABCMeta):

    @abstractmethod
    def foo(self):
        pass


class Child(MyBaseClass):
    pass

c = Child()
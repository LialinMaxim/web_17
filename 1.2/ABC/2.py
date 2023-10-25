from abc import abstractmethod, ABCMeta, ABC


class MyBaseClass(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass


class Child(MyBaseClass, ABC):
    ...

    # def foo(self):
    #     print('__foo')
    #     ...


c = Child()
c.foo()

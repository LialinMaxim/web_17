class MyABC:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()


class A(MyABC):
    pass


a = A().bar()
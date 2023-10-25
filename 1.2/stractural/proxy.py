class API:
    @staticmethod
    def request():
        print("request")


class MyAPI:
    @staticmethod
    def request():
        print("MY request")


class Proxy:
    def __init__(self, obj) -> None:
        self._obj = obj

    def request(self) -> None:
        if self.check_access():
            self._obj.request()
            self.log_access()

    def check_access(self) -> bool:
        print("check_access")
        return True

    def log_access(self) -> None:
        print("log_access")


def client_code(subject):
    subject.request()


if __name__ == "__main__":
    # no proxy
    real_subject = API()
    client_code(real_subject)

    print("___with proxy_____", '\n')
    #
    # proxy = Proxy(real_subject)
    # client_code(proxy)

    proxy2 = Proxy(MyAPI())
    client_code(proxy2)

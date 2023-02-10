from abc import ABC, abstractmethod


class Target(ABC):
    """
    The Target defines the domain-specific interface used by the client code.
    """

    @abstractmethod
    def request(self) -> str:
        pass


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """
    print(target.request())


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)

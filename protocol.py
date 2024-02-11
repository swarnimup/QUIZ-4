from typing import Protocol

class MyBaseProtocol(Protocol):
    def method1(self) -> None:
        pass

    def method2(self) -> None:
        pass

class SubClass1:
    def method1(self) -> None:
        print("Implementation of method1 in SubClass1")

    def method2(self) -> None:
        print("Implementation of method2 in SubClass1")

class SubClass2:
    def method1(self) -> None:
        print("Implementation of method1 in SubClass2")

    def method2(self) -> None:
        print("Implementation of method2 in SubClass2")

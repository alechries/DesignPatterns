from __future__ import annotations
from abc import ABC, abstractmethod


# Abstract classes


class AbstractHandler(ABC):
    @abstractmethod
    def set_next_handler(self, handler: AbstractHandler) -> AbstractHandler:
        pass

    @abstractmethod
    def request_handle(self, request: str):
        pass


# Concrete classes


class ConcreteHandler(AbstractHandler):
    _next_handler = None

    def __init__(self, handle_type: str):
        self.__handle_type = handle_type

    def set_next_handler(self, handler: AbstractHandler):
        self._next_handler = handler
        return handler

    def request_handle(self, request: str):
        if self.__handle_type in request:
            print(f"I'm {self.__handle_type}-handler and I can work with {self.__handle_type}")
        elif self._next_handler is not None:
            print(f"I'm {self.__handle_type}-handler and I don't can work with {self.__handle_type}")
            self._next_handler.request_handle(request)


class ConcreteHandlerA(ConcreteHandler):
    def __init__(self):
        super().__init__('A')


class ConcreteHandlerB(ConcreteHandler):
    def __init__(self):
        super().__init__('B')


class ConcreteHandlerC(ConcreteHandler):
    def __init__(self):
        super().__init__('C')


class ConcreteHandlerD(ConcreteHandler):
    def __init__(self):
        super().__init__('D')


# Using


handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_c = ConcreteHandlerC()
handler_d = ConcreteHandlerD()
handler_a.set_next_handler(handler_b).set_next_handler(handler_c).set_next_handler(handler_d)
handler_a.request_handle('D')
# Output:
# I'm A-handler and I don't can work with A
# I'm B-handler and I don't can work with B
# I'm C-handler and I don't can work with C
# I'm D-handler and I can work with D

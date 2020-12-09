from abc import ABC, abstractmethod


# Abstract classes

class AbstractWorker(ABC):
    @abstractmethod
    def operation_process(self):
        pass


class AbstractManager(ABC):
    def __init__(self, worker: AbstractWorker):
        self.worker = worker

    @abstractmethod
    def operation(self):
        pass


# Concrete classes


class ConcreteWorkerA(AbstractWorker):
    def operation_process(self):
        print("Operation process with worker A")


class ConcreteWorkerB(AbstractWorker):
    def operation_process(self):
        print("Operation process with worker B")


class ConcreteManagerA(AbstractManager):
    def operation(self):
        print("Operation with manager A")
        self.worker.operation_process()


class ConcreteManagerB(AbstractManager):
    def operation(self):
        print("Operation with manager B")
        self.worker.operation_process()


# Using

worker_a: AbstractWorker = ConcreteWorkerA()
worker_b: AbstractWorker = ConcreteWorkerB()
manager_a: AbstractManager = ConcreteManagerA(worker_a)

manager_a.operation()  # Output: Operation with manager A
#                                Operation process with worker A
manager_a.worker = worker_b
manager_a.operation()  # Output: Operation with manager A
#                                Operation process with worker B


from abc import ABC, abstractmethod

from order import Order


class PaymentProcessor(ABC):
    @abstractmethod
    def execute(self, order: Order) -> None:
        raise NotImplementedError

from abc import ABC, abstractmethod

from order import Order


class PaymentProcessor(ABC):
    @abstractmethod
    def execute(self, order: Order, security_code: str) -> None:
        raise NotImplementedError

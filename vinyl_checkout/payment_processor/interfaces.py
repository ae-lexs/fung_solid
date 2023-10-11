from abc import ABC, abstractmethod

from order import Order


class PaymentProcessor(ABC):
    @abstractmethod
    def execute(self, order: Order) -> None:
        raise NotImplementedError


class MasterCardPaymentProcessor(PaymentProcessor):
    @abstractmethod
    def sms_validation(self, sms_code: str):
        raise NotImplementedError

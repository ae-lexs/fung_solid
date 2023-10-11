from abc import ABC, abstractmethod


class OrderManager(ABC):
    @abstractmethod
    def add_item(
        self,
        name: str,
        price: float,
        quantity: int,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def total_price(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def processed(self):
        raise NotImplementedError

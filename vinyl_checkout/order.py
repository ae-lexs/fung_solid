from typing import List

from entity.errors import InvalidPaymentMethodError
from entity.enums import OrderStatus, PaymentMethod


class Order(object):
    items: List[str] = []
    prices: List[float] = []
    quantities: List[int] = []
    status: OrderStatus = OrderStatus.PENDING

    def add_item(self, name: str, price: float, quantity: int) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def total_price(self) -> float:
        total = 0

        for index in range(len(self.prices)):
            total += self.quantities[index] * self.prices[index]
        
        return round(total, 2)

    def pay(self, payment_method: str, security_code: str):
        if payment_method == PaymentMethod.DEBIT.value:
            print('Processing Debit Payment Type')
            print('Verifying Security Code: {security_code}'.format(
                security_code=security_code,
            ))
            self.status = OrderStatus.PROCESSED
        elif payment_method == PaymentMethod.CREDIT.value:
            print('Processing Credit Payment Type')
            print('Verifying Security Code: {security_code}'.format(
                security_code=security_code,
            ))
            self.status = OrderStatus.PROCESSED
        else:
            raise InvalidPaymentMethodError

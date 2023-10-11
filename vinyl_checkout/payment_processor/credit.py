from order import Order
from payment_processor.interfaces import PaymentProcessor


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code

    def execute(self, order: Order) -> None:
        print('Processing Credit Payment Method')
        print('Total: {order_total}'.format(
            order_total=order.total_price(),
        ))
        print('Verifying Security Code: {security_code}'.format(
            security_code=self.security_code,
        ))
        order.processed()

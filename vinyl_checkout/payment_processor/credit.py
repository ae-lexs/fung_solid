from order import Order
from payment_processor.interfaces import PaymentProcessor


class CreditPaymentProcessor(PaymentProcessor):
    def execute(self, order: Order, security_code: str) -> None:
        print('Processing Credit Payment Method')
        print('Verifying Security Code: {security_code}'.format(
            security_code=security_code,
        ))
        print('Total: {order_total}'.format(
            order_total=order.total_price(),
        ))
        order.processed()

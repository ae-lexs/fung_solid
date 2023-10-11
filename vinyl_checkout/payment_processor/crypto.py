from order_manager.interfaces import OrderManager
from payment_processor.interfaces import PaymentProcessor


class CryptoPaymentProcessor(PaymentProcessor):
    def __init__(self, email: str):
        self.email = email

    def execute(self, order: OrderManager) -> None:
        print('Processing Crypto Payment Method')
        print('Total: {order_total}'.format(
            order_total=order.total_price(),
        ))
        print('Verifying Account: {email}'.format(
            email=self.email,
        ))
        order.processed()

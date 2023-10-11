from order_manager.interfaces import OrderManager
from payment_processor.interfaces import MasterCardPaymentProcessor


class CreditPaymentProcessor(MasterCardPaymentProcessor):
    def __init__(self, security_code: str):
        self.security_code = security_code

    def sms_validation(self, sms_code: str):
        print('SMS Validation Code: {sms_code}'.format(
            sms_code=sms_code,
        ))

    def execute(self, order: OrderManager) -> None:
        print('Processing Credit Payment Method')
        self.sms_validation(sms_code='893251')
        print('Total: {order_total}'.format(
            order_total=order.total_price(),
        ))
        print('Verifying Security Code: {security_code}'.format(
            security_code=self.security_code,
        ))
        order.processed()

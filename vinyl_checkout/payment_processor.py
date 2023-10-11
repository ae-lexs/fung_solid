from entity.errors import InvalidPaymentMethodError
from entity.enums import PaymentMethod
from order import Order


class PaymentProcessor(object):
    def execute(
        self,
        order: Order,
        payment_method: str,
        security_code: str,
    ):
        if payment_method == PaymentMethod.DEBIT.value:
            print('Processing Debit Payment Method')
            print('Verifying Security Code: {security_code}'.format(
                security_code=security_code,
            ))
            print('Total: {order_total}'.format(
                order_total=order.total_price(),
            ))
            order.processed()
        elif payment_method == PaymentMethod.CREDIT.value:
            print('Processing Credit Payment Method')
            print('Verifying Security Code: {security_code}'.format(
                security_code=security_code,
            ))
            print('Total: {order_total}'.format(
                order_total=order.total_price(),
            ))
            order.processed()
        else:
            raise InvalidPaymentMethodError

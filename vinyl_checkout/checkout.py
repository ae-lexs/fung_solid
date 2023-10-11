from entity.enums import PaymentMethod
from order import Order
from payment_processor import PaymentProcessor


class Checkout(object):
    def execute(self):
        order = Order()
        payment_processor = PaymentProcessor()

        order.add_item(
            name='Alvvays, Blue Rev',
            price=100.20,
            quantity=1,
        )
        order.add_item(
            name='The Beatles, Revolver',
            price=300.20,
            quantity=1,
        )
        order.add_item(
            name='Bjork, Vespertine, Vinyl',
            price=200.20,
            quantity=1,
        )

        print('Order Status: {order_status}'.format(
            order_status=order.status.value,
        ))

        payment_processor.execute(
            order=order,
            payment_method=PaymentMethod.DEBIT.value,
            security_code='120b4',
        )

        print('Order Status: {order_status}'.format(
            order_status=order.status.value,
        ))


Checkout().execute()

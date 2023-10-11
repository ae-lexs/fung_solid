from entity.enums import PaymentMethod
from order_manager.interfaces import OrderManager
from order_manager.amazon import AmazonOrderManager
from payment_processor.interfaces import PaymentProcessor
from payment_processor.factory import get_payment_processor


class Checkout(object):
    def execute(self):
        order: OrderManager = AmazonOrderManager()
        payment_processor: PaymentProcessor = get_payment_processor(
            payment_method=PaymentMethod.CRYPTO,
            security_code='120b4',
            email='alexis@gmail.com',
        )

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
        )

        print('Order Status: {order_status}'.format(
            order_status=order.status.value,
        ))


Checkout().execute()

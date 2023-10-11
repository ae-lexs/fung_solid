from order import Order
from entity.enums import PaymentMethod


class Checkout(object):
    def execute(self):
        order = Order()
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

        print('Total Price {total_price}'.format(
            total_price=order.total_price(),
        ))

        order.pay(
            payment_method=PaymentMethod.DEBIT.value,
            security_code='120b4',
        )


Checkout().execute()

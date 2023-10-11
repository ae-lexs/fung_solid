from entity.enums import PaymentMethod
from entity.errors import InvalidPaymentMethodError

from payment_processor.interfaces import PaymentProcessor
from payment_processor.credit import CreditPaymentProcessor
from payment_processor.crypto import CryptoPaymentProcessor
from payment_processor.debit import DebitPaymentProcessor


def get_payment_processor(
    payment_method: PaymentMethod,
) -> PaymentProcessor:
    if payment_method == PaymentMethod.DEBIT:
        return DebitPaymentProcessor()
    elif payment_method == PaymentMethod.CREDIT:
        return CreditPaymentProcessor()
    elif payment_method == PaymentMethod.CRYPTO:
        return CryptoPaymentProcessor()
    else:
        raise InvalidPaymentMethodError

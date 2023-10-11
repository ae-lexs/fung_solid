from typing import Optional

from entity.enums import PaymentMethod
from entity.errors import InvalidPaymentMethodError

from payment_processor.interfaces import PaymentProcessor
from payment_processor.credit import CreditPaymentProcessor
from payment_processor.crypto import CryptoPaymentProcessor
from payment_processor.debit import DebitPaymentProcessor


def get_payment_processor(
    payment_method: PaymentMethod,
    email: Optional[str] = None,
    security_code: Optional[str] = None,
) -> PaymentProcessor:
    if payment_method == PaymentMethod.DEBIT:
        return DebitPaymentProcessor(
            security_code=security_code,
        )
    elif payment_method == PaymentMethod.CREDIT:
        return CreditPaymentProcessor(
            security_code=security_code,
        )
    elif payment_method == PaymentMethod.CRYPTO:
        return CryptoPaymentProcessor(
            email=email,
        )
    else:
        raise InvalidPaymentMethodError

from enum import Enum


class OrderStatus(Enum):
    PENDING = 'PENDING'
    PROCESSED = 'PROCESSED'


class PaymentMethod(Enum):
    CREDIT = 'CREDIT'
    CRYPTO = 'CRYPTO'
    DEBIT = 'DEBIT'

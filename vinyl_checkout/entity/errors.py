class InvalidPaymentMethodError(Exception):
    def __init__(self):
        super().__init__('INVALID_PAYMENT_METHOD')

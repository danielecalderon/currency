
class Currency:
    def __init__(self, Currency_code, value):
        self.value = currencey
        self.currency = currency
    def __add___(self, Currency_code, value):
        return '{} plus {}'.format(self.value, value)

class DifferentCurrencyCodeError (Exception):
    pass

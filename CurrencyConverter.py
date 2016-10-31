print("Lets convert you money!\n")

currencies = {"USD":"(US Dollar)",
             "EUR":"(Euro)",
             "SDQ":"(Dominican Rep.)",
             "GBP":"(Great Britain Pound)"}
for keys,values in currencies.items():
    print(keys)

    print(values)
conversion = input("Choose your (From) country 'A' and you 'To' country 'B' ")
    #if conversion = input("How much?")


Currency_code = {"USD": 1.0, "EUR":0.91,
"SDQ":.02, "GBP": .82}


class CurrencyConverter():
    def __init__(self, Currency_code, value):
        self.value = value
        self.currency = currency
    def __add___(self, Currency_code, value):
        return '{} plus {}'.format(self.value, value)

#currencey_converter.covert(Currency(1, USD), 'USD') == Currency(1, USD'')

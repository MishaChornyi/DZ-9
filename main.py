import requests
class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate
    def convert_to_usd(self, amount):
        return amount / self.exchange_rate

def get_exchange_rate():
    url = 'https://finance.i.ua/'
    response = requests.get(url)
    exchange_rate = 38.4083 #1 USD = 38.4083 гривень

    return exchange_rate

def main():
    exchange_rate = get_exchange_rate()
    converter = CurrencyConverter(exchange_rate)

    amount = float(input("Введіть кількість валюти твоєї країни: "))
    converted_amount = converter.convert_to_usd(amount)

    print(f"{amount} вашої валюти дорівнює {converted_amount:.2f} доларам США.")

if __name__ == "__main__":
    main()

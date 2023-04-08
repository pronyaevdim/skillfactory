import json
import requests
from config import exchanges


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        #
        # if base != exchanges[base.lower()]:
        #     raise APIException(f' не верно ввели значение {base}!')
        # if sym != exchanges[sym.lower()]:
        #     raise APIException(f' не верно ввели значение {sym}!')
        try:
            base = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base  == sym :
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        headers = {"apikey": "QlmEOIfFUQijRRYY5dDws2yo44m8b9PT"}
        r = requests.get(f"https://api.apilayer.com/exchangerates_data/latest?symbols={sym}&base={base}", headers=headers)
        resp = json.loads(r.content)
        new_price = resp['rates']
        # new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {sym} : {new_price}"
        return message
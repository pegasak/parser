# -*- coding: utf-8 -*-

from requests import Request, Session
import json


def get_crypto_info():
    """
        Получает информацию о пяти топовых криптовалютах с использованием CoinMarketCap API.
        :param result_str: хранит в себе результат выполнения функции, то есть запаршенные данные
        :param name: название криптовалюты
        :param price: актуальная цена криптовалюты
        :param market_cap: капитализация криптовалюты
        Returns:
        str: Строка с информацией о криптовалютах в формате "Имя - Цена: <цена>, Рыночная капитализация: <рыночная капитализация>".
    """
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'limit': 10
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'c704f8c3-7200-4299-8ec1-88c936ffa6b9'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    data = json.loads(response.text)['data']

    name_and_price_list = []
    for index in range(10):
        name = data[index]['name']
        price = data[index]['quote']['USD']['price']
        market_cap = data[index]['quote']['USD']['market_cap']
        price_with_symbol = f"{price}$"
        market_cap_with_symbol = f"${market_cap:,}$"
        name_and_price_list.append({'name': name, 'price': price_with_symbol, 'market_cap': market_cap_with_symbol})

    result_str = "\n".join(
        [f"{item['name']} - Цена: {item['price']}, Рыночная капитализация: {item['market_cap']}" for item in
         name_and_price_list])
    return result_str


res = get_crypto_info()
print(res)

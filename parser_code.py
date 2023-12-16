# -*- coding: utf-8 -*-

from requests import Request, Session
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'limit': 5
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
for index in range(5):
    name = data[index]['name']
    price = data[index]['quote']['USD']['price']
    market_cap = data[index]['quote']['USD']['market_cap']
    price_with_symbol = f"{price}$"  # Добавляем значок доллара
    market_cap_with_symbol = f"${market_cap:,}$"  # Добавляем значок доллара и форматируем числовое значение
    name_and_price_list.append({'name': name, 'price': price_with_symbol, 'market_cap': market_cap_with_symbol})

# Красивый вывод без скобок и запятых
for item in name_and_price_list:
    print(f"{item['name']} - Цена: {item['price']}, Рыночная капитализация: {item['market_cap']}")

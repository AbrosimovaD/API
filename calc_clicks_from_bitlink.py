from dotenv import load_dotenv
import os
import requests
from urllib.parse import urlparse

MAIN_LINK = 'https://api-ssl.bitly.com/v4/'


def shorten_link(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    link = f'{MAIN_LINK}bitlinks'
    body = {'long_url': url}
    response = requests.post(link, json=body, headers=headers)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    link = f'{MAIN_LINK}bitlinks/{url}/clicks/summary'
    response = requests.get(link, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    link = f'{MAIN_LINK}bitlinks/{url}'
    return requests.get(link, headers=headers).ok


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    url = input('Введите ссылку: ')
    url_sh = f'{urlparse(url).netloc}{urlparse(url).path}'
    if is_bitlink(url_sh, token):
        try:
            clicks_count = count_clicks(token, url_sh)
        except requests.exceptions.HTTPError:
            print('Операция завершена с ошибкой')
        else:
            print(f'По Вашей ссылке перешли {clicks_count} раз(а)')
    else:
        try:
            bitlink = shorten_link(token, url)
        except requests.exceptions.HTTPError:
            print('Операция завершена с ошибкой')
        else:
            print(f'Битлинк: {bitlink}')


if __name__ == '__main__':
    main()

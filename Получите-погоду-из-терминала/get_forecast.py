import requests


URL = 'https://wttr.in'


def get_weather(countries):
    params = {
        'lang' : 'ru',
        'M':'',
        'm':'',
        'n':'',
        'q':'',
        'T':''
    }
    for place in countries:
        response = requests.get(f'{URL}/{place}', params = params)
        response.raise_for_status()
        print(response.text)
    return

def main():
  countries = ['london', 'svo', 'череповец']
  get_weather(countries)

if __name__ == '__main__':
    main()

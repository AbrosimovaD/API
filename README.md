# Космический Телеграм




## Окружение
* Python 3
  
## Зависимости
Все необходимые библиотеки находятся в файле *requirements.txt*.

Если файл находится в той же директории, что и файл скрипта, то для установки воспользуйтесь командой 

  ```  pip install -r requirements.txt ```

Если же в другой папке - необходимо дополнительно прописать путь до файла:

  ``` pip install -r /path/to/requirements.txt ```

## Переменные окружения
В данном скрипте для выполнения запросов используется переменная окружения ```BITLY_TOKEN=*персональный токен с сайта Bitly*```.

### Как получить
1. Первым делом Вам необходимо создать аккаунт на сайте [Bit.ly](https://bitly.com/) (если у Вас его нет).

1. При запросе сайт запрашивает токен авторизации - его необходимо сгенерировать во вкладке [Settings -> Developer Settings -> API](https://app.bitly.com/settings/api/)  :
![image](https://github.com/AbrosimovaD/API/assets/114830550/05f3da6b-62c2-4cf2-9563-69cdd0e3cf16)

1. После чего создайте переменную окружения на своём компьютере:
    1. создайте специальный файл ```.env``` рядом с ```main.py```. Внутри файлы ```.env``` похожи на списки из переменных и их значений:
      ```BITLY_TOKEN=*сгененированный токен из предыдущего шага*```

## Запуск скрипта
Запустить скрипт можно обычным способом. Например, через командную строку:

```  python3 calc_clicks_from_bitlink.py  ```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).



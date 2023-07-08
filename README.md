# Создание битлинков и подсчет кликов по ним
Скрипт просит на ввод ссылку.

Если введена обычная (длинная) ссылка, то выводится ее укороченная версия - битлинк.
![image](https://github.com/AbrosimovaD/API/assets/114830550/8d29b04e-f325-4b66-b3b5-10fb2f34a553)

Если же введен битлинк, то подсчитывается суммарное количество кликов по ней.
![image](https://github.com/AbrosimovaD/API/assets/114830550/6661474e-49a6-46ab-ae54-589fbdccf9e7)

*Если Ваш аккаунт на [Bit.ly](https://bitly.com/) бесплантный, то суммируется только за интервал в 30 дней.*

**Также у бесплатного аккаунта есть ограничение на создание битлинков - 10 штук в месяц**

## Чтобы код не сломался
* Все необходимые библиотеки находятся в файле *requirements.txt*.

  Если файл находится в той же директории, что и файл скрипта, то для установки воспользуйтесь командой 

  ```  pip install -r requirements.txt ```

  Если же в другой папке - необходимо дополнительно прописать путь до файла:

  ``` pip install -r /path/to/requirements.txt ```

* Python 3
  
## Запуск скрипта
1. Первым делом Вам необходимо создать аккаунт на сайте [Bit.ly](https://bitly.com/) (если у Вас его нет).

1. При запросе сайт запрашивает токен авторизации - его необходимо сгенерировать во вкладке [Settings -> Developer Settings -> API](https://app.bitly.com/settings/api/)  :
![image](https://github.com/AbrosimovaD/API/assets/114830550/05f3da6b-62c2-4cf2-9563-69cdd0e3cf16)

1. После чего создайте переменную окружения на своём компьютере:
    1. создайте специальный файл ```.env``` рядом с ```main.py```. Внутри файлы ```.env``` похожи на списки из переменных и их значений:
      ```BITLY_TOKEN=*сгененированный токен из предыдущего шага*```

1. Ура! Вся подготовка сделана. Можно запускать программу обычным способом. Например, через командную строку:

```  python3 calc_clicks_from_bitlink.py  ```

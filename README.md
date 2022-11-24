![Иллюстрация к проекту](https://github.com/dvdkitay/python-checker-call-sip/temp/screen.png)

Проект для тестирования и проверки рабочих добавочных номеров на удаленном номере. Настроен с транком Megafon, но можно исправить под любого провайдера, необходимо изменить данные в `install/sip.conf` перед установкой.

Работает в многопоточном режиме. Колличество запущенных потоков зависит от колличества добавочных номеров в файле.

Программа работает в цикле и каждые 150 номеров делает паузу в две минуты. Данное решение добавлено для настройки динамической нагрузки на сервер.

## Установка

Перенести проект на сервер и перейти в папку проекта

```
cd python-checker-call-sip
```

```
cd install
```

Запуск установки
```
chmod +x install.sh
```

```
./install.sh
```

## Настройка конфигурации 

Вписать добавочные номера в файле `extension_numbers.txt` (каждый добавочный с новой строки)

```
nano configuration/extension_numbers.txt
```

Вписать необходимые данные в файле `config.py`

```
nano configuration/config.py
```

Вписать `NUMBER` и `PASSWORD` данные в файле `config.py`

```
nano install/sip.conf
```

## Проверка добавочных номеров на телефоне

При запуске удаляется файл статистики звонков Asterisk по пути `/var/log/asterisk/cdr-csv/Master.csv`

```
python3 app.py
```

## Проверка результатов после работы

```
python3 show.py
```

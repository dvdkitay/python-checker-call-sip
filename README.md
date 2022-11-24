<div align="left">
<img src="https://img.shields.io/github/languages/code-size/dvdkitay/python-checker-call-sip" />
<img src="https://img.shields.io/github/languages/top/dvdkitay/python-checker-call-sip" />
<img src="https://img.shields.io/github/issues/dvdkitay/python-checker-call-sip" />
<img src="https://img.shields.io/github/issues-pr/dvdkitay/python-checker-call-sip" />

<div>

```
[SCRIPT-DEBUG] INFO: Скрипт запущен
[SCRIPT-DEBUG] INFO: Обнаружено 3 добавочных номеров
[SCRIPT-DEBUG] INFO: Конфигурация запущена
[SCRIPT-DEBUG] INFO: Файл статистики Asterisk очищен
[SCRIPT-DEBUG] INFO: Файл результатов очищен
[SCRIPT-DEBUG] INFO: Начало работы
[SCRIPT-DEBUG] INFO: Работаем по добавочному номеру: 1
[SCRIPT-DEBUG] INFO: Запущен поток pid: 42769 для добавочного: 1
[SCRIPT-DEBUG] INFO: Работаем по добавочному номеру: 2
[SCRIPT-DEBUG] INFO: Запущен поток pid: 42772 для добавочного: 2
[SCRIPT-DEBUG] INFO: Работаем по добавочному номеру: 3
[SCRIPT-DEBUG] INFO: Запущен поток pid: 42775 для добавочного: 3
[SCRIPT-DEBUG] INFO: Рабочие: 3, Не рабочие: 0
```

Проект для тестирования и проверки рабочих добавочных номеров на удаленном номере. Настроен с транком Megafon, но можно исправить под любого провайдера, необходимо изменить данные в `install/sip.conf` перед установкой.

Работает в многопоточном режиме. Колличество запущенных потоков зависит от колличества добавочных номеров в файле.

Программа работает в цикле и каждые 150 номеров делает паузу в две минуты. Данное решение добавлено для настройки динамической нагрузки на сервер.

## Настройка конфигурации 

Перенести проект на сервер и перейти в папку проекта

```
cd python-checker-call-sip
```

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

## Установка

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

## Проверка добавочных номеров на телефоне

При запуске удаляется файл статистики звонков Asterisk по пути `/var/log/asterisk/cdr-csv/Master.csv`

```
python3 app.py
```

Результат работы

```
[SCRIPT-DEBUG] INFO: Скрипт запущен
[SCRIPT-DEBUG] INFO: Обнаружено 3 добавочных номеров
[SCRIPT-DEBUG] INFO: Конфигурация запущена
[SCRIPT-DEBUG] INFO: Файл статистики Asterisk очищен
[SCRIPT-DEBUG] INFO: Файл результатов очищен
[SCRIPT-DEBUG] INFO: Начало работы
[SCRIPT-DEBUG] INFO: Работаем по добавочному номеру: 1
[SCRIPT-DEBUG] INFO: Запущен поток pid: 42769 для добавочного: 1
[SCRIPT-DEBUG] INFO: Работаем по добавочному номеру: 2
[SCRIPT-DEBUG] INFO: Запущен поток pid: 42772 для добавочного: 2
[SCRIPT-DEBUG] INFO: Работаем по добавочному номеру: 3
[SCRIPT-DEBUG] INFO: Запущен поток pid: 42775 для добавочного: 3
[SCRIPT-DEBUG] INFO: Рабочие: 3, Не рабочие: 0
```

## Проверка результатов после работы

```
python3 show.py
```

Результат работы

```
[SCRIPT-DEBUG] INFO: Добавочный 1 Статус: True
[SCRIPT-DEBUG] INFO: Добавочный 2 Статус: True
[SCRIPT-DEBUG] INFO: Добавочный 3 Статус: True
```
</div>
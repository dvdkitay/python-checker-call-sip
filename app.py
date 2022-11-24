import subprocess
import time
import logging
import sys
import os
import csv 
import json 
import shutil

from configuration.config import NUMBER_CALLING, CALLER_ID, ANSWER_WAIT, ANSWER_DTMF_WAIT, WORK_DTMF_SECONDS

logging.basicConfig(
    format='[SCRIPT-DEBUG] %(levelname)s: %(message)s',
    level=logging.INFO
)
        
logging.info(f"Скрипт запущен")

def csv_to_json(csvFilePath, jsonFilePath, WORK_DTMF_SECONDS):
    jsonArray = []
      
    with open(csvFilePath, encoding='utf-8') as csvf: 

        for row in csvf: 
            row = row.split(",")
            
            jsonArray.append(
                {"extension_number": row[8].split(":")[1],
                "seconds": row[13],
                "status_calling": row[14],
                "status": True if float(row[13]) > int(WORK_DTMF_SECONDS) else False}
            )
  
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
          
def subprocess_func(NUMBER_CALLING, CALLER_ID, extension_numbers, ANSWER_WAIT, ANSWER_DTMF_WAIT) -> bool:
    
    commond = f"/usr/bin/python3 call.py {NUMBER_CALLING} {CALLER_ID} {extension_numbers} {ANSWER_WAIT} {ANSWER_DTMF_WAIT}"
    try:
        pid = subprocess.Popen(
            args=commond,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            preexec_fn=os.setsid
        )
    except Exception as error:
        return False
    return pid

def start(NUMBER_CALLING, CALLER_ID, ANSWER_WAIT, ANSWER_DTMF_WAIT, WORK_DTMF_SECONDS):
    
    file_extension_numbers = "configuration/extension_numbers.txt"

    quantity = sum(1 for line in open(file_extension_numbers, 'r'))

    logging.info(f"Обнаружено {quantity} добавочных номеров")
    
    i = 0
     
    try:

        logging.info(f"Конфигурация запущена")
        
        shutil.copy2("temp/Master.csv", '/var/log/asterisk/cdr-csv/Master.csv')
        logging.info(f"Файл статистики Asterisk очищен")
        time.sleep(3)
        os.remove("temp/result.json")
        logging.info(f"Файл результатов очищен")
        time.sleep(3)
        logging.info(f"Начало работы")
        
        with open(file_extension_numbers, "r") as FILE:

            for extension_number in FILE.readlines():
                # Колличество проходов
                i = i + 1
                
                extension_number_temp = extension_number.replace("\n", "")
                logging.info(f"Работаем по добавочному номеру: {extension_number_temp}")
                
                sub = subprocess_func(
                    NUMBER_CALLING, CALLER_ID, extension_number_temp,
                    ANSWER_WAIT, ANSWER_DTMF_WAIT
                )
                
                if not sub:
                    logging.error(
                        f"Ошибка запуска потока. Добавочный номер: {extension_number_temp}"
                    )

                logging.info(f"Запущен поток pid: {sub.pid} для добавочного: {extension_number_temp}")
                
                if i == 150:
                    time.sleep(120)
                    logging.info(f"Запущено 150 звонков делаем паузу в 2 минуты")
                    
                    i = 0 
                
                time.sleep(0.6)
        
        time.sleep(int(ANSWER_WAIT) + int(ANSWER_DTMF_WAIT) + 12)
        
        csvFilePath = r'/var/log/asterisk/cdr-csv/Master.csv'
        jsonFilePath = r'temp/result.json'
        
        csv_to_json(csvFilePath, jsonFilePath, WORK_DTMF_SECONDS)
        
        json_file_path = "temp/result.json"

        working = 0
        dont_working = 0
        
        with open(jsonFilePath) as j:
            result = json.loads(j.read())
            
            for r in result:
                if r["status"]:
                    working = working + 1
                else:
                    dont_working = dont_working + 1
                    
        
    except Exception as error:
        logging.error(error)
        
    return working, dont_working

if __name__ == '__main__':
    
    try:
        res = os.system("asterisk -rx 'module load chan_sip.so'")
    except Exception as error:
        pass
    
    working, dont_working = start(
        NUMBER_CALLING, CALLER_ID, ANSWER_WAIT, ANSWER_DTMF_WAIT, WORK_DTMF_SECONDS
    )
    
    logging.info(
        f"Рабочие: {working}, Не рабочие: {dont_working}"
    )
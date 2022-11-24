import json
import logging

json_file_path = "temp/result.json"

logging.basicConfig(
    format='[SCRIPT-DEBUG] %(levelname)s: %(message)s',
    level=logging.INFO
)

try:
    with open(json_file_path, 'r') as j:
        contents = json.loads(j.read())
        
        for c in contents:
            logging.info(
                f"Добавочный {c['extension_number']} Статус: {c['status']}"
            )   
except Exception as error:
    logging.error("Ошибка работы программы")
    
     
    
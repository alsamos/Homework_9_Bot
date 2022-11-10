import time
import json


def read_from_json(db_path):
    with open(db_path, "r", encoding="UTF-8") as source:
        text = source.read()
        if text:
            return text  
        else: 
            return "В файле отсутствуют данные"


def append_to_json(db_path, db_list):
    with open(db_path, 'a', encoding="UTF-8") as source:
        source.write(" ".join(db_list) + "\n")
    print(f"\nДанные сохранены в {db_path}.\n")
    time.sleep(1)
    return
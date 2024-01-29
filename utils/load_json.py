import json


def load_operations(filename):
    """
    Загружает список операций из файла

    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)




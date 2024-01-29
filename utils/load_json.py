import json


def load_operations():
    """
    Загружает список операций из файла

    """
    with open("../operations.json", "r", encoding="utf-8") as file:
        return json.load(file)




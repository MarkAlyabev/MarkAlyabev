# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    d = []
    with open(INPUT_FILENAME, 'r', encoding='utf-8')
        r = csv.DictReader(f) #каждая строка словарь
        for i in r:
            d.append(i) #добавляем строку в список
    with open (OUTPUT_FILENAME, 'w', encoding='utf-8') as f: #записываем в json файл
        json.dump(d, f, indent=4, ensure_ascii=False) #записываем список словарей в файл json, устанавливаем нужные отступы, и чтобы буквы верные

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

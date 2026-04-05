import json #подключаем модуль
def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f: #открываем файл для чтения
        d = json.load(f)  # превращаем в список словарей
    k = 0  #переменная для суммы
    for i in d:
        k += i['score'] * i['weight']  #умножаем и прибавляем к сумме
    return round(k, 3)  #возвращаем с огруглением


print(task())

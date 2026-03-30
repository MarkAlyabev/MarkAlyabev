# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    if find_item in items_list:
        index_item = items_list.index(find_item)
        #используем метод index(), которая определяет индекс первого вхождения искомого слова и присваиваем это значение переменой
    else:
        index_item = None
        # если слово не входит в список значение переменной становится None
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

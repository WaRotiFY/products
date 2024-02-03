import csv

# Открываем файл products.csv
with open('products.csv', encoding = 'utf-8') as data:
    reader = list(csv.reader(data, delimiter = ';'))
    table_names = reader[0]
    table = reader[1:]
    new_table = table[:]
    last_sum=0 # Общая выручка с закуски
    i=0
    # Цикл по каждой строчке файла
    for category, product, date, price_per_unit, count in table:
        get_money = str(float(price_per_unit)*float(count)) # Находим выручку
        new_table[i].append(get_money)
         # Проверяем: 'Является ли продукт закуской'? Если да, добавляем в общую выручку с закуски
        if category == 'Закуски':
            last_sum+=float(get_money)
        i+=1
    print(last_sum)

# Создаем новый файл products_new.csv с измененными данными
with open('products_new.csv', mode = 'w', encoding = 'utf-8') as data:
    writer = csv.writer(data, delimiter = ';', lineterminator = '\r')
    writer.writerow(table_names+['total'])
    writer.writerows(new_table)



        


























    

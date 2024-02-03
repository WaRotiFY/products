import csv

# Открываем файл products.csv
with open('products.csv', encoding = 'utf-8') as data:
    reader = list(csv.reader(data, delimiter = ';'))
    table_names = reader[0]
    table = reader[1:]
    hash_table={}
    # Цикл по каждой строчке файла
    for category, product, date, price_per_unit, count in table:
        if category in hash_table.keys():
            hash_table[category] += float(count)
        else:
            hash_table[category]=0
            hash_table[category] += float(count)
        
    sorted_item = sorted(hash_table.items(), key=lambda x:x[1])
    for i in range(10):
        print(f'{sorted_item[i][0]}, {sorted_item[i][1]}')

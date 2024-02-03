import csv

alf_up = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯ'

# Открываем файл products.csv
with open('products.csv', encoding = 'utf-8') as data:
    reader = list(csv.reader(data, delimiter = ';'))
    table_names = reader[0]
    table = reader[1:]
    for i in range(1, len(table)):
        trash_let_data = alf_up.index(table[i][0][0])
        trash_data = table[i]
        for x in range(i-1,-1,-1):
            if trash_let_data<alf_up.index(table[x][0][0]):
                table[x+1] = table[x]
            else:
                table[x] = trash_data
                break
            if x==0:
                table[x] = trash_data
    # Цикл по каждой строчке файла
    check_category = table[0][0]
    m_product = ''
    m_price_per_unit = -(10**10)
    for category, product, date, price_per_unit, count in table:
        if check_category == category:
            if m_price_per_unit<float(price_per_unit):
                m_product = product
                m_price_per_unit = float(price_per_unit)
    print(f'В категории: {check_category} самый дорогой товар: {m_product} его цена за единицу товара составляет {price_per_unit}')
        
        

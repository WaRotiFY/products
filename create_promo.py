import csv

# Функция для создания купона
def createPromo(name, date):
    alf_low = 'абвгдеёжзийклмнопрстуфхцчшщьъыэюя'
    alf_up = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЫЭЮЯ'
    """
        Описание аргументов:
        
        name - название товара
        date - дата посткупления товара

    """
    spl_date = date.split('.')
    rev_month = spl_date[1][1] + spl_date[1][0]
    product = ''
    for x in name:
        if x not in alf_up and x != ' ':
            product += alf_up[alf_low.index(x)]
        elif x==' ':
            pass
        else:
            product += x
    rev_last_let = product[-1] + product[-2]
    let = product[0] + product[1]
    day = spl_date[0]
    promo = let + day + rev_last_let + rev_month
    return promo
    
# Открываем файл products.csv
with open('products.csv', encoding = 'utf-8') as data:
    reader = list(csv.reader(data, delimiter = ';'))
    table_names = reader[0]
    table = reader[1:]
    new_table = table[:]
    i=0
    # Цикл по каждой строчке файла
    for category, product, date, price_per_unit, count in table:
        new_table[i].append(createPromo(product, date))
        i += 1

# Создаем новый файл products_promo.csv с измененными данными
with open('products_promo.csv', mode = 'w', encoding = 'utf-8') as data:
    writer = csv.writer(data, delimiter = ';', lineterminator = '\r')
    writer.writerow(table_names+['promocode'])
    writer.writerows(new_table)



















        

import csv

# Открываем файл products.csv
with open('products.csv', encoding = 'utf-8') as data:
    reader = list(csv.reader(data, delimiter = ';'))
    table_names = reader[0]
    table = reader[1:]
    inp_data = input('Введите категорию: ').lower
    # Цикл, запрашивающий категурию
    while inp_data != 'молоко':
        less_product = ''
        less_count = 10**10
        isCategory = 0
        # Цикл по каждой строчке файла
        for category, product, date, price_per_unit, count in table:
            if inp_data == category:
                if less_count>float(count):
                    less_product = product
                    less_count = float(count)
                isCategory=1
        if isCategory:
            print(f'В категории: {inp_data} товар: {less_product} был куплен {less_count} раз')
        else:
            print('Такой категории не существует в нашей БД')
        inp_data = input('Введите категорию: ')
                
                    
            
        

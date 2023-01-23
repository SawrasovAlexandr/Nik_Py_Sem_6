# Берет данные из файла(path_file) и возвращает в виде списка словарей

# было
# def init(path_file: str) -> list:
#     with open(path_file, 'r', encoding = 'UTF-8') as database:
#         temp_list = database.read().split('\n')
#     list_of_dict = []
#     for item in temp_list:
#         temp = item.split(';')
#         list_of_dict.append({'Фамилия': temp[0], 'Имя': temp[1],'Телефон': temp[2], 'Комментарий': temp[3]})
#     return list_of_dict

# стало
def init(path_file: str) -> list:
    with open(path_file, 'r', encoding = 'UTF-8') as database:
        temp_list = database.read().split('\n')
    list_of_dict = [dict(zip(['Фамилия', 'Имя', 'Телефон', 'Комментарий'], item.split(';'))) for item in temp_list]
    return list_of_dict

# Ищет строку(find_str) в значениях словарей списка(data_base) и если находит, то выводит их и их индексы в data_base в консоль

# было
# def find_cont(find_str: str, data_base: list) -> list:
#     find_data = []
#     for item in data_base:
#         if find_str.lower() in ' '.join(item.values()).lower():
#             find_data.append(item)
#     for item in find_data:
#         i = data_base.index(item)
#         item = list(item.values())
#         print(f'{i:4} | {item[0]:13} | {item[1]:10} | {item[2]:12} | {item[3]}')  
    
# стало
def find_cont(find_str: str, data_base: list) -> list:
    find_data = list(filter(lambda item: find_str.lower() in ' '.join(item[1].values()).lower(), enumerate(data_base)))
    for item in find_data:
        i = item[0]
        item = list(item[1].values())
        print(f'{i:4} | {item[0]:13} | {item[1]:10} | {item[2]:12} | {item[3]}') 


def main():
    db = init('database.csv')
    find_cont('Дмитрий', db)


if __name__ == '__main__':
    main()
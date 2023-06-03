file_name = 'country_info.txt'

country_dict = {}

with open(file_name, 'r', encoding='UTF-8') as country_file:
    for row in country_file:
        data = row.rstrip().split('|')
        # print(data)
        country_dict[data[0].casefold()] = data

# print('Slownik:')
# print(country_dict)

while True:
    selected_country = input('Podaj nazwę Kraju: ').casefold()
    if selected_country == '0' or selected_country == '' or selected_country == 'exit':
        break
    print('Wybrany Kraj:', country_dict.get(selected_country)[0])
    print('Stolica:', country_dict.get(selected_country)[1])
    print('Kod kraju:', country_dict.get(selected_country)[2])
    print('Strefa czasowa:', country_dict.get(selected_country)[5])
    print('Waluta:', country_dict.get(selected_country)[6])
    print()

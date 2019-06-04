import re

file1, file2 = 'winedata_1.json', 'winedata_2.json'
full_json = 'winedata_full.json'

import re
def merge_write_json(file1, file2):
    """
    Открывает файлы, читает их и склеиваем это всё в одну
    строку, а потом записываем, ну и попутно немного подчищаем.
    :param file1:
    :param file2:
    :return:
    """
    with open(file1, 'r', encoding='utf-8') as f1, \
            open(file2, 'r', encoding='utf-8') as f2:
        # merge, clean and write down to single file
        text = f'{f1.read()[:-1]},{f2.read()[1:]}'
        with open('winedata_full.json', 'w', encoding='utf-8') as out:
            json = text.replace('null', '"0"')
            out.write(json)

    return json


def cleaning(filename):
    """
    Берет фаил, читает его, далее выковыривает все что м/у {}
    и это у нас становится СПИСКОМ!!! потом мы проходимся по
    этому списку и доковыриваем 'price', опять таки используем
    шаблон и если в цене НЕ ноль, то подсовываем его в спискок значений,
    ну и в конце делаем словарик и пихаем его в wine_data. Всё, все данные готовы!
    :param filename:
    :return: wine_data
    """
    json = open(filename, encoding='utf-8').read()
    by_elems = re.findall(r'\{(.*?)\}', json)

    k = [
        'points',
        'title',
        'description',
        'taster_name',
        'taster_twitter_handle',
        'price',
        'designation',
        'variety',
        'region_1',
        'region_2',
        'province',
        'country',
        'winery',
         ]

    wine_data = []  # will hold all data
    for elem in by_elems:
        values = re.findall(r'\: \"(.*?)\"', elem)      # get values
        values[0] = int(values[0])  # we need digit not str don't you?
        if '"price": "0"' not in elem:
            price = list(map(int, re.findall(r'\"price\"\: (.*?)\,', elem)))
            if price[0] > 0:
                values.insert(5, price[0])
        temp_dict = dict(zip(k, values))
        wine_data.append(temp_dict)

    # sort by price from big to small
    wine_data = sorted(wine_data, key=lambda x: int(x['price']), reverse=True)

    # print(re.findall(r'\"(.*?)\"\: \"', first))     # get keys
    with open('winedata_full.json', 'w', encoding='utf-8') as out:
        json = f'{wine_data}'
        out.write(json)

    return wine_data


def avarage_price(variety, wine_data):
    price = [int(x['price']) for x in wine_data if x['variety'] == variety and int(x['price']) > 0]
    if len(price) == 0:
        print(f'\tAvarage price for {variety} is: ', 0)
        return 0

    avg_price = round(sum(price)/len(price), 2)
    return avg_price


def min_price(variety, wine_data):
    price = [int(x['price']) for x in wine_data if x['variety'] == variety and int(x['price']) > 0]
    if len(price) == 0:
        print(f'\tMinimum price for {variety} is: ', 0)
        return 0

    minimum_price = min(price)
    print(f'\tMinimum price for {variety} is: ', minimum_price)
    return minimum_price


def max_price(variety, wine_data):
    price = [int(x['price']) for x in wine_data if x['variety'] == variety and int(x['price']) > 0]
    if len(price) == 0:
        print(f'\tMaximum price for {variety} is: ', 0)
        return 0
    max_price = max(price)
    print(f'\tMaximum price for {variety} is: ', max_price)
    return max_price


def most_common_region(variety, wine_data):
    region_1 = [x['region_1'] for x in wine_data if x['variety'] == variety and x['region_1'] != '0']
    region_2 = [x['region_2'] for x in wine_data if x['variety'] == variety and x['region_2'] != '0']
    regions = region_1 + region_2
    most_common = {}
    keys = list(set(regions))
    for region in keys:
        r = region
        kye = [r]
        v = [regions.count(region)]
        tmp_d = dict(zip(kye, v))
        most_common.update(tmp_d)

    count = 0
    name = ''
    for key in most_common.keys():
        if most_common[key] > count:
            count = most_common[key]
            name = key

    print(f'\tMost common region for {variety} is: ', name, count)


def most_common_country(variety, wine_data):
    countries = [x['country'] for x in wine_data if x['variety'] == variety and x['country'] != '0']
    most_common = {}
    keys = list(set(countries))
    # print(countries)
    # print(keys)
    for country in keys:
        r = country     # need to be assign as a string for first
        kye = [r]
        v = [countries.count(country)]
        tmp_d = dict(zip(kye, v))
        most_common.update(tmp_d)

    count = 0
    name = ''
    for key in most_common.keys():
        if most_common[key] > count:
            count = most_common[key]
            name = key

    print(f'\tMost country region for {variety} is: ', name, count)

def avarage_score(variety, wine_data):
    points = [int(x['points']) for x in wine_data if x['variety'] == variety and int(x['points']) > 0]
    if len(points) == 0:
        print(f'\tAvarage score for {variety} is: ', 0)
        return 0
    avg_points = round(sum(points)/len(points), 2)
    print(f'\tAvarage score for {variety} is: ', avg_points)
    return avg_points


if __name__ == '__main__':
    varietys = ['Gew\\u00fcrztraminer', 'Riesling', 'Merlot', 'Tempranillo', 'Red Blend', 'Madera']
    # varietys = ['Gew\\u00fcrztraminer']

    def main(wines, variety=None):
        print(f'Statistics for {variety}:')

        avarage_price(variety, wines)
        min_price(variety, wines)
        max_price(variety, wines)
        most_common_region(variety, wines)
        most_common_country(variety, wines)
        avarage_score(variety, wines)

        print('. . . . . . . . . . . . . . . \n')

    merge_write_json(file1, file2)
    wines = cleaning(full_json)

    for variety in varietys:
        main(wines, variety=variety)

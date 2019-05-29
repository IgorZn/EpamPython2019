import re
def merge_write_json(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, \
            open(file2, 'r', encoding='utf-8') as f2:

        # merge, clean and write down to single file
        text = f'{f1.read()[:-1]},{f2.read()[1:]}'
        with open('winedata_full.json', 'w', encoding='utf-8') as out:
            json = text.replace('null', 'None')
            out.write(json)

    return json


# find all {<key: value>}
json = merge_write_json('winedata_1.json', 'winedata_2.json')
by_elems = re.findall(r'\{(.*?)\}', json)
print(by_elems)


# parsing all data to dict
my_dict = {}
for a, elem in enumerate(by_elems):
    # prepare string and split
    splited_elems = elem.split(', "')
    temp_list = []

    for i, s_elem in enumerate(splited_elems):
        # prepare string and split
        list_elms = splited_elems[i].strip().replace('"', '').split(':')
        try:
            value = int(list_elms[1])
        except ValueError:
            value = list_elms[1]
        key = list_elms[0]
        temp_list.append((key, value))

    t_dict = dict(temp_list)    # dict = dict([(1, 100), (2, 400)]) -> {1: 100, 2: 400}
    my_dict.update({a: t_dict})

last_num = list(my_dict.keys())[-1]

# check for duplicates
for i in range(last_num):
    if my_dict.get(i) == my_dict.get(i+1):
        print(my_dict.get(i), my_dict.get(i+1))
        my_dict.pop(i+1)

print(my_dict)
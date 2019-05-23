import re

with open('winedata_1.json', 'r', encoding='utf-8') as f1, \
        open('winedata_2.json', 'r', encoding='utf-8') as f2:

    text = f1.read()[:-1] + ',' + f2.read()[1:]
    with open('winedata_full.json', 'w', encoding='utf-8') as out:
        out.write(text)

# merge and write down to single file
with open('winedata_full.json', encoding='utf-8') as f:
    json = f.read()[1:-1].replace('null', 'None')

# find all {<key: value>}
by_elems = re.findall(r'\{(.*?)\}', json)

# parsing all data to dict
my_dict = {}
for a, elem in enumerate(by_elems):
    splited_elems = elem.split(', "')
    temp_list = []

    for i, s_elem in enumerate(splited_elems):
        list_elms = splited_elems[i].strip().replace('"', '').split(':')
        try:
            value = int(list_elms[1])
        except ValueError:
            value = list_elms[1]
        key = list_elms[0]
        temp_list.append((key, value))

    t_dict = dict(temp_list)
    my_dict.update({a: t_dict})

last_num = list(my_dict.keys())[-1]

# check for duplicates
for i in range(last_num):
    if my_dict.get(i) == my_dict.get(i+1):
        print(my_dict.get(i), my_dict.get(i+1))
        my_dict.pop(i+1)




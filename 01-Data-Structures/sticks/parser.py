with open('winedata_1.json', 'r', encoding='utf-8') as f1, open('winedata_2.json', 'r', encoding='utf-8') as f2:
    text = f1.read()[:-1] + ',' + f2.read()[1:]
    with open('winedata_full.json', 'w', encoding='utf-8') as out:
        out.write(text)

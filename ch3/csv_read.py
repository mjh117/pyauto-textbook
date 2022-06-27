import csv, pprint

# csv 모듈을 이용하지 않는 방법 --- (1)
with open('./input/items.csv', encoding='ansi') as f:
    text = f.read().strip()
    lines = text.split("\n")
    data = [v.split(',') for v in lines]
    pprint.pprint(data)

# csv 모듈을 이용하는 방법 --- (2)
with open('./input/items.csv', encoding='ansi') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
    pprint.pprint(data)
    

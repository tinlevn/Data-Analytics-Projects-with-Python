#JD is the mastermind behind this simple program. 
#I learned a lot from him. 
import csv
from pathlib import Path
from itertools import groupby
def get_transactions(path):
    with open(Path(path), 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        trans_dict = {}
        for row in reader:
            if not trans_dict.get(row['type']):
                trans_dict[row['type']] = [row]
            else:
                trans_dict[row['type']].append(row)
    return trans_dict

#Change file path according to your machine please. 
trans = get_transactions("Sacramentorealestatetransactions.csv")
min_trans = []
max_trans = []
for k, v in trans.items():
    sorted_trans = sorted(v, key=lambda x: int(x['price']))
    min_trans.append((sorted_trans[0]['type'], int(sorted_trans[0]['price'])))
    max_trans.append((sorted_trans[-1]['type'], int(sorted_trans[-1]['price'])))

print(min_trans)
print(max_trans)

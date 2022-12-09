import csv

data = []
filename = './data/gsb202211GS.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append({
            "datetime": row[1],
            "location": row[4],
            "price": row[7]
        })

print(data)

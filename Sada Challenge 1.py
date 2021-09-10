import csv
import json

rows_to_remove = []
rows_to_keep = []
# opens the csv file
with open('data.csv') as data:
    data_file = csv.DictReader(data)
    line_num = 1
    # creating new dic for csv file
    fields = ['Year','Rank', 'Company', 'Revenue (in millions)', 'Profit (in millions)']
    for row in data_file:
        line_num += 1
        try:
            row['Profit (in millions)'] = float(row['Profit (in millions)'])
            rows_to_keep.append(row)
        except ValueError:
            row['Profit (in millions)'] = str(row['Profit (in millions)'])
            rows_to_remove.append(row)

print()
print(line_num)
print()
print(len(rows_to_keep))
print()

with open ('data2.json', 'w') as new_json:
    json.dump(rows_to_keep, new_json)

with open('data2.json') as j:
    data2 = json.load(j)

sorted_data2 = sorted(data2, key=lambda x: x['Profit (in millions)'], reverse=True)

for row in range(20):
    print(sorted_data2[row])

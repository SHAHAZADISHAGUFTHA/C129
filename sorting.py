import csv
data = []

with open("newData.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

print(data[0])
headers = data[0] 
planet_data = data[1:]
for datapoint in planet_data:
    try:
        datapoint[2] = datapoint[2].lower()
    except IndexError:
       pass
    continue
planet_data.sort(key = lambda planet_data:planet_data[2])
with open ("new_data_sorted.csv","a+") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

import csv
data1 = []
data2 =[]
with open("data1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data1.append(row)
with open("new_data_sorted.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data2.append(row)
header1 = data1[0]
planet_data_1 = data1[1:]
header2 = data2[0]
planet_data_2 = data2[1:]
headers = header1 + header2
planet_data = []
for index,data_row in enumerate(planet_data_1):
        planet_data.append(planet_data_1[index]+planet_data_2[index])
with open ("final_data.csv","a+") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
        
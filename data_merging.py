import csv 

dataset1=[]
dataset2=[]

with open("dwarf_stars.csv","r") as f:
    csvread=csv.reader(f)
    for row in csvread:
        dataset1.append(row)

with open("bright_stars.csv","r") as f:
    csvread=csv.reader(f)
    for row in csvread:
        dataset2.append(row)

header1=dataset1[0]
data1=dataset1[1:]

header2=dataset2[0]
data2=dataset2[1:]

header=header1+header2
data=[]

for index,datarow in enumerate(data2):
    data.append(data1[index]+data2[index])
    

with open("merged_data.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(data)
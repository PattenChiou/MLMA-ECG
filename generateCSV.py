import csv
import os

allData = []
training = os.listdir("./data_new/training")
validation = os.listdir("./data_new/validation")
with open("./data/REFERENCE.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        allData.append(i)
with open("./data_new/training/REFERENCE.csv", "w") as f:
    writer = csv.writer(f)
    for i in allData:
        if i[0]+".mat" in training:
            writer.writerow(i)
with open("./data_new/validation/REFERENCE.csv", "w") as f:
    writer = csv.writer(f)
    for i in allData:
        if i[0]+".mat" in validation:
            writer.writerow(i)
import csv

number_Primary_Type = 0
number_Date = 0
max_number = 0
dict = {}
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if number_Primary_Type == 0:
            for ro in row:
                if ro == "Primary Type":
                    break
                number_Primary_Type = number_Primary_Type + 1
            for ro in row:
                if ro == "Date":
                    break
                number_Date = number_Date + 1
        if "/2015" in row[number_Date]:
            if row[number_Primary_Type] in dict.keys():
                dict[row[number_Primary_Type]] = dict[row[number_Primary_Type]] + 1
            else:
                dict[row[number_Primary_Type]] = 1
for dic in dict:
    if dict[dic] > max_number:
        max_number = dict[dic]
        name_Primary = dic
print(name_Primary)

import csv

def loadAbbreviations():
    data_list = []
    
    with open('dataFiles/abbreviation.csv', mode='r') as file:
    
        csv_reader = csv.reader(file)
        header = next(csv_reader, None)
    
        for row in csv_reader:
            data_list.append(row)

    dictFormat = {}

    for i in data_list:
        key = str(i[0].upper())
        val = str(i[1])

        dictFormat[key] = val
    
    # print(dictFormat)
    return dictFormat



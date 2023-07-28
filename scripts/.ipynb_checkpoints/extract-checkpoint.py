import numpy as np
import csv

def getBatchDetails(data, batch):

    ans = []
    
    for i in data.keys():
        for j in data[i]:

            if(len(j) < 5): continue

            for k in range(1, len(j)):
                if(j[k - 1] == batch[0] and j[k] == batch[1]):
                    ans.append(i)
                
    return ans   

def beautifyData(data):
    ans = {}

    for i in data:
        for j in range(1, len(i)):
            
            lst = (i[0], j)

            if lst in ans:
                ans[lst].append(i[j])
            else:
                ans[lst] = [i[j]]

    return ans

def loadData():
    data_list = []
    
    with open('data.csv', mode='r') as file:
    
        csv_reader = csv.reader(file)
        header = next(csv_reader, None)
    
        for row in csv_reader:
            data_list.append(row)

    return data_list


data = loadData()
mappedData = beautifyData(data_list)

batchData = getBatchDetails(mappedData, 'F8')

print(batchData)
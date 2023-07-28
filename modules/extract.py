# import numpy as np
import csv
import re

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def formatTextData(t, s):

    s = ''.join(s.split())
    s += '$'

    obj = []

    obj.append(t)

    if s[0] == 'L':
        obj.append('Lecture')
    elif s[1] == 'T':
        obj.append('Tutorial')
    else:
        obj.append('Practical')

    subjectData = re.search('\((.*)\)', s)
    obj.append(subjectData.group(1))

    classRoom = re.search('-(.*)/', s)
    obj.append(classRoom.group(1))

    teacher = re.search('/(.*)\$', s)
    obj.append(teacher.group(1))

    # print(obj)
    return obj


def reformat(a):

    ans = []

    timeSlots = [[]]
    for i in range(8):

        startTime = i + 9
        startTime %= 12

        if startTime == 0:
            startTime += 12
        
        startTime = str(startTime)
        if len(startTime) == 1:
            startTime = '0' + startTime

        timeSlots.append(startTime + ':00 - ' + startTime + ':50')
    
    ans.append(timeSlots)

    for i in a.keys():
        
        dict = {}
        for j in range(1, 9):
            dict[j] = [timeSlots[j], '', '', '', '']

        for j in a[i]:
            if(len(j) != 1):
                dict[j[0]] = formatTextData(timeSlots[j[0]], j[1])

        tmpPush = []
        for j in dict.keys():
            tmpPush.append(dict[j])
        
        ans.append(tmpPush)
    
    # print(ans)
    return ans


def getBatchDetails(data, key):
    batch = key['input']
    day = key['day']

    ans = {}
    btch = batch

    for i in days:
        ans[i] = []
    
    for i in data.keys():
        for j in data[i]:

            if(len(j) < 5): 
                ans[i[0]].append([i[1]])
                continue

            for k in range(1, len(j)):
                if(j[k - 1] == batch[0] and j[k] == batch[1]):
                    ans[i[0]].append([i[1], j])

    formattedAns = reformat(ans)
    formattedAns = list(formattedAns[days.index(day) + 1])
    
    return formattedAns

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
    
    with open('dataFiles/data.csv', mode='r') as file:
    
        csv_reader = csv.reader(file)
        header = next(csv_reader, None)
    
        for row in csv_reader:
            data_list.append(row)

    return beautifyData(data_list)
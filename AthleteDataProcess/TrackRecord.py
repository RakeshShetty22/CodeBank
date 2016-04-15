"""This script for the reading the athlethe track record and do a data
massage and pull the reports"""
def ReadData(fileName):
    listData = []
    try:
        with open(fileName,'r') as fHandler:
          data = fHandler.readline() 
        listData = data.strip().split(',')      
    except:
        print("There was an exception !!!... ")
    return listData

def SanitizeData(dataVal):
    if '-' in dataVal:
        splitter = '-'
    elif ':' in dataVal:
        splitter = ':'
    else:
        return(dataVal)
    (mins, secs) = dataVal.split(splitter)
    return(mins + '.' + secs)
    
james = ReadData('james.txt')
julie = ReadData('julie.txt')
mikey = ReadData('mikey.txt')
sarah = ReadData('sarah.txt')

"""print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))"""

newJamesList = sorted([SanitizeData(dat) for dat in james])
newJulieList = sorted([SanitizeData(dat) for dat in julie])
newMikeyList = sorted([SanitizeData(dat) for dat in mikey])
newSarahList = sorted([SanitizeData(dat) for dat in sarah])

print(newJamesList)
print(newJulieList)
print(newMikeyList)
print(newSarahList)

"""uniqueJameData = []
for eachItem in newJamesList:
    if eachItem not in uniqueJameData:
        uniqueJameData.append(eachItem)"""

print(sorted(set(newJamesList))[0:3])


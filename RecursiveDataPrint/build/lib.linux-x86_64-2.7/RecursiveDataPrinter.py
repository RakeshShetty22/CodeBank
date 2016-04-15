"""This file is used for printing the n level list using recursive method"""

def NestDataPrinter(dataToPrint):
    for eachItem in dataToPrint:
        if(isinstance(eachItem,list)):
            NestDataPrinter(eachItem)
        else:
            print(eachItem)


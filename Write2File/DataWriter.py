"""This script is used for writing the data to files"""

import pickle
list = ["a","b","c","d"]
try:
    with open('datafile.txt','wb') as fHandler:
        pickle.dump(list,fHandler)

    with open('datafile.txt','rb') as fRHandler:
        alist = pickle.load(fRHandler)
    print (alist)
except:
    print("There was a error during the processing....")


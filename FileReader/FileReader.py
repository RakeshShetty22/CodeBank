"""This python script is used for reading a file and re-arranging the data"""

import os

try:
  print(os.getcwd())  
  dataFile = open('DataFile.txt')
  
  for data in dataFile:
      try:
          (role, info) = data.split(':',1)
          print role,
          print " :said ",
          print info
      except ValueError:
          pass

  dataFile.close()
except IOError:
    print("Please check the file. File doesn't exist")

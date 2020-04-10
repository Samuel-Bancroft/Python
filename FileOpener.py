import os
import shutil
import csv
from FileChanger.functions import *

path = "C:\\Users\\Samuel Bancroft\\PycharmProjects\\AnAIApproachToVariedDataSets\\FileChanger\\DataSet_Test_Folde\\"
newpath = "C:\\Users\\Samuel Bancroft\\PycharmProjects\\AnAIApproachToVariedDataSets\\FileChanger\\DataSet_NewTest_Folder\\"

csv_file = []
files = []
imagefiles = []
try:
    for r, d, f in os.walk(path):
        for file in f:
            if ".txt" in file:
                #can just put shutil in the if block to make code shorter
                files.append(os.path.join(r, file))
            elif ".png" in file:
                imagefiles.append(os.path.join(r, file))
            elif ".csv" in file:
                csv_file.append(os.path.join(r, file))
                with open(file) as csvFile:
                    csvFile = csv.reader(csvFile, deliminiter = ",")
                    attributeType = next(csvFile)
                    print(attributeType)
        for x in files:
            shutil.move(x, newpath)
        for x in imagefiles:
            shutil.move(x, newpath)
        for x in csv_file:
            shutil.move(x, newpath)

    for x in files:
        print(x)
    for x in csv_file:
        print(x)

    #for x in imagefiles:
     #   if ".png" in x:
      #      displayimages(x)

    """
    for f in files:
        readable = open(f, "r")
        print(f)
        print(readable.read())
    """
except:
    print(Exception)
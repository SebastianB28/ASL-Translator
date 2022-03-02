import os
import random
from csv import writer

numberTrain = 30

numberTest = 30

dataDir = "letterDirectory/rawData"

folders = os.listdir("letterDirectory/rawData")

#headers = ["Letter", "File Name", "Thumb", "Index", "Middle", "Ring", "Pinky","Yaw","Pitch","Roll"]
headers = ["Letter", "File Name", "Pinky", "Ring", "Middle", "Index", "Thumb"]

trainFile = "letterDirectory/trainData.csv"

testFile = "letterDirectory/testData.csv"

with open (trainFile, "w+") as dataset:
    writerObj = writer(dataset)
    writerObj.writerow(headers)
    dataset.close()

with open (testFile, "w+") as dataset:
    writerObj = writer(dataset)
    writerObj.writerow(headers)
    dataset.close()

for folder in folders:
    newPath = os.path.join(dataDir + "/" + folder)

    files = os.listdir(newPath)
    random.shuffle(files)

    for index in range(0,numberTrain):
        file = files[0]
        filePath = os.path.join(dataDir + "/" + folder + "/" + file)

        dataFile = open(filePath, "r")

        data = dataFile.readline()
        dataFile.close()

        dump = folder + "," + file + "," + data
        dump = dump.split(",")

        with open (trainFile, "a", newline='') as dataset:
            writerObj = writer(dataset)
            writerObj.writerow(dump)
            dataset.close()

        files.pop(0)
        
        print(dump)

    for index in range((30 - numberTest),30):
        file = files[0]
        filePath = os.path.join(dataDir + "/" + folder + "/" + file)

        dataFile = open(filePath, "r")

        data = dataFile.read()
        dataFile.close()

        dump = folder + "," + file + "," + data
        dump = dump.split(",")

        with open (testFile, "a", newline='') as dataset:
            writerObj = writer(dataset)
            writerObj.writerow(dump)
            dataset.close()

        files.pop(0)

        print(dump)

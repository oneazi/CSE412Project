import csv
import json
from Deserializer import Artist
from Deserializer import ArtistAlbums
from Deserializer import Track
from Deserializer import Album


#writer class that adds entries into CSV sheets
class CSVWriter:

    #inserts a row into a CSV sheet
    def writeToCSV(self, row, typeOfEntity):
        filePath = "C:/Users/Andy/Desktop/412/csv/" + typeOfEntity + ".csv"

        #Adds a new album entry to the top of the CSV 
        with open(filePath, "r", encoding='utf-8') as readfile:
    
            reader = csv.reader(readfile)
            lines = list(reader)
            
            lines.insert(1, row)

        with open(filePath, 'w', newline = '', encoding='utf-8') as writefile:  
            csvwriter = csv.writer(writefile) 
            csvwriter.writerows(lines)

        writefile.close()
        readfile.close()

    def addLabel(self, labelName):
        filePath = "C:/Users/Andy/Desktop/412/csv/Label.csv"
        alreadyStored = False
        firstLoop = True
        secondLoop = False
        currentMaxID = -1
        with open(filePath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if(secondLoop):
                    currentMaxID = row[0]
                    firstLoop = False
                    secondLoop = False
                if(firstLoop):
                     secondLoop = True
                if(row[1] == labelName):
                    alreadyStored = True
        
        if(not alreadyStored):
            newMaxId = int(currentMaxID) + 1
            row = [str(newMaxId), str(labelName)]
            self.writeToCSV(row, "Label")
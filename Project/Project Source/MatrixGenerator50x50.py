# -*- coding: utf-8 -*-
"""
Created on Sat May 15 16:48:24 2021

@author: Ertuğrul Demir
"""

import numpy as np

def MapGenerator(startRow, startColumn, stopRow, stopColumn, obs_rate):
    
    mapMatrix=[]
    
    #Creating 50 row
    for i in range(50):      
        mapMatrix.append(randomRowCreate())
    
    #Adding Obstacle
    
    mapMatrix=obstacleGenerate(mapMatrix,obs_rate)
    #Setting clour of  start point and stop point.
    mapMatrix[startRow][startColumn]=(mapMatrix[startRow][startColumn][0],"BLUE")
    mapMatrix[stopRow][stopColumn]=(mapMatrix[startRow][stopColumn][0],"BLUE")

    return mapMatrix
def obstacleGenerate(mapMatrix, obs_rate):
    obsCount=0    
    while(obsCount<(50*50*obs_rate)):
        #Rastgele
        Row=np.random.randint(50)
        Column=np.random.randint(50)
        if(mapMatrix[Row][Column][1]!="RED"):
            mapMatrix[Row][Column] =(mapMatrix[Row][Column][0],"RED")
            obsCount+=1
    return mapMatrix
    
def randomRowCreate():
    # Size --> 50  => 50 elemanlı bir vektör. (50 stunu olan bir satır gibi düşünülebilir.)
    Row = list(np.random.randint(11, size=50))    
    newRow=[]
    #rate_Obstacle = 15
    #obstacleCount =0
        
    for i in Row:
        column = (i,"WHITE")
        newRow.append(column)
    return newRow


def Drawer(mapMatrix):
    for i in range(len(mapMatrix)):
        print(i," : " , mapMatrix[i] )



def printMapToTextFile(mapMatrix):
    with open("engel.txt","w") as f:
        counter=1
        for row in mapMatrix:
            f.write(str(counter)+":"+str(row)+"\n")
            counter+=1


#Testing
"""
myMap=MapGenerator(0, 0, 10, 10)
printMapToTextFile(myMap)
print("Start point \n",myMap[0][0])
print(myMap[0][0][0],"," ,myMap[0][0][1])

print("\n\nStop point \n",myMap[10][10])
print(myMap[10][10][0],"," ,myMap[10][10][1])      



           
            if(np.random.randint(10)==5 and (obstacleCount < rate_Obstacle)):
                #True ise Kırmızı olsun --> Engel
                column = (i,"RED")
                obstacleCount +=1
                
            else:
                #False ise Beyaz  olsun --> Boşluk
                column = (i,"WHITE")
           

 
"""




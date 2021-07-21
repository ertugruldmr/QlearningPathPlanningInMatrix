# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:31:22 2021

@author: Ertuğrul Demir
"""

from tkinter import Tk, Canvas, Frame, BOTH
import MatrixGenerator50x50 as MAP
import QL
import matplotlib.pyplot as plt

class Example(Frame):

    def __init__(self,mapMatrix):
        super().__init__()
        self.mapMatrix=mapMatrix
        self.initUI()


    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        
        #Map starting points of draw
        size=15
        x_start=35
        y_start=35   

        #Lines
        for Row in range(51):
            #i=Row
            #canvas.create_rectangle(x_start+((i-1)*size), y_start+((i-1)*size),x_start+(i*size) , y_start+(i*size), fill="blue", width=2)
      
            
            canvas.create_line(x_start, y_start+size*Row, x_start+(size*50), y_start+size*Row)
        for Column in range(51):
            
            canvas.create_line(x_start+size*Column, y_start, x_start+size*Column, y_start+(50*size))
        #Matrix Indexes
        for i in range(1,51):        
            #Row index
            Row_start_X =x_start+(size//2)
            Row_start_Y =y_start-(size//2)
            canvas.create_text(Row_start_X+((i-1)*size),Row_start_Y, text=str(i))
            
            #Column index
            Row_start_X =x_start- (size//2)
            Row_start_Y =y_start+ (size//2)
            canvas.create_text(Row_start_X, Row_start_Y+ ((i-1)*size) , text=str(i))

        
        #Map içeriği ekrana yansıtılırken.
        for Row in range(0,50):
            for Column in range(0,50):
                Value,colour=self.mapMatrix[Row][Column]
                
                #creating colour for rectangle
                canvas.create_rectangle(x_start+(Column*size), y_start+(Row*size),x_start+((Column+1)*size) , y_start+((Row+1)*size), fill=colour, width=2)
                #creating value in rectangle
                canvas.create_text(Row_start_X+size+ ((Column)*(size)), Row_start_Y+ ((Row)*(size)) , text=Value)
                
        
        #Show images
        canvas.pack(fill=BOTH, expand=1)
        
        
        
        


def main():
    
    
    # Consol Inputs
    while True:
        try:
            start_row=int(input("Başlangıç noktasının Satırını giriniz :"))     -1
            start_column=int(input("Başlangıç noktasının Stununu giriniz :"))   -1
            target_row =int(input("Hedef noktasının Satırını giriniz :"))       -1
            target_column =int(input("Hedef noktasının Stununu giriniz :"))     -1
            obs_rate=float(input("Engel oranını giriniz: "))
            #-1 --> index starts 0 (out of index error [case : 50 > 49])
            # CASE : Start != Stop
            isSamePosition=(start_row == target_row) and (start_column==target_column)
            #Boolean cases
            SR=start_row > 50 or start_row < 0
            SC=start_column > 50 or start_column < 0
            TR=target_row > 50 or target_row < 0
            TC=target_column > 50 or target_column < 0
            Orate= obs_rate>1.0 or obs_rate< 0.0
            
            # Results --> Excepting casess
            result=(SR or SC or TR or TC or Orate or isSamePosition)
            if (result):
                #•print("SR:",SR,"\nSC",SC,"\nTR",TR,"\nTC",TC,"\nOrate",Orate,"\nisSamePosition",isSamePosition)
                raise 
            
            break
        except:
            print("*"*50)
            print("Lütfen Sayı şunlara  dikkat edin :")
            print("*"*50)
            print("\n-->Sayı girin.\n-->50X50 arası konum 0-1 arası oran verin.\n-->Aynı konumları girmeyin")

    
    root = Tk()
    myMap=MAP.MapGenerator(start_row, start_column, target_row, target_column,obs_rate)
    #path=Qlearning.FindPath(start_row,start_column,target_row,target_column,myMap)
    path = QL.Find(start_row,start_column,target_row,target_column,myMap)
    print("Optimum path")
    print(path)
    
    optimumPath=[]
    tmp_max_Revard=0
    ID=int()
    EvS=list()
    EvR=list()
    for ep,isTargetCaptured,pathReward,Ep_Path in path:
        if(isTargetCaptured):
            EvS.append(len(Ep_Path))
            EvR.append(pathReward)
            if(tmp_max_Revard < pathReward):
                tmp_max_Revard =pathReward
                ID=ep
                optimumPath=Ep_Path
                final=[ep,isTargetCaptured,pathReward,Ep_Path]
    print("optimumPath:",optimumPath)    
    
    for stateStep in optimumPath:
        R,C = QL.StateToR_C(stateStep)
        myMap[R][C] = (myMap[R][C][0],"BLUE")
    
    ex = Example(myMap)
    MAP.printMapToTextFile(myMap)
    
    
    """      
    # plotting the points 
    plt.plot(range(len(path)), EvS)
    plt.xlabel('Episode')
    plt.ylabel('Step')
    plt.title('Episode via Step')
      
    # function to show the plot
    plt.show()
    """

    # Initialise the subplot function using number of rows and columns
    figure, axis = plt.subplots(1, 2)
      
    # For Sine Function
    axis[0].plot(range(len(EvS)), EvS)
    axis[0].set_title("Episode via Step")
      
    # For Cosine Function
    axis[1].plot(range(len(EvR)), EvR)
    axis[1].set_title("Episode via Reward")    
    
    plt.show()
    
    root.geometry("1920x1080+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 19:57:47 2021

@author: Ertuğrul Demir
"""

def IsInMatrixRange(index):
    return (0<=index) and (50>index)
def MatrixRowColumnTOstateIDConverter(Row,Column):
    if(IsInMatrixRange(Row) and IsInMatrixRange(Column)):    
        return (Column+1)+(Row*50)
    else:
        raise
def StateToR_C(state):
    if(state>0):
        #R = (state - (state // 51 )*50)// 51
        if(state % 50 != 0):
            C= state % 50
        else:
            C= 50
        
        if(state % 50 != 0):
            R= state // 50
        else:
            R= (state //50) -1
            
        
        
        #R=
        #C= (state - (state // 51 )*50) % 51
        # R&C start at 0 index
        return [R,C-1]
    else:
        return [1,1]
""" 
testing   IsInMatrixRange, MatrixRowColumnTOstateIDConverter, StateToR_C
  
for Row in range(50):
    for Column in range(50):
        print(Row,",",Column," -->  ",MatrixRowColumnTOstateIDConverter(Row, Column))
      
for state in range(1,500):
    print(state," --> ", StateToR_C(state))
"""

#Action Coder
def ActionCoder(Acs_list):
    Coded=[]
    for ac in Acs_list:
        if(ac == "Up"):Coded.append(1)
        if(ac == "Down"):Coded.append(2)
        if(ac == "Left"):Coded.append(3)
        if(ac == "Right"):Coded.append(4)
        
        if(ac == "UL"):Coded.append(5)
        if(ac == "UR"):Coded.append(6)
        if(ac == "DL"):Coded.append(7)
        if(ac == "DR"):Coded.append(8)
    
    if(len(Coded) == len(Acs_list)):
        return Coded
#Action Decoder
def ActionDecoder(Acs_list):
    Decoded=[]
    for ac in Acs_list:
        if(ac == 1):Decoded.append("Up")
        if(ac == 2):Decoded.append("Down")
        if(ac == 3):Decoded.append("Left")
        if(ac == 4):Decoded.append("Right")
        
        if(ac == 5):Decoded.append("UL")
        if(ac == 6):Decoded.append("UR")
        if(ac == 7):Decoded.append("DL")
        if(ac == 8):Decoded.append("DR")
    
    if(len(Decoded) == len(Acs_list)):
        return Decoded    


"""
testing ActionCoder,ActionDecoder


Raw_Action = ["Up","Down","Left","Right","UL","UR","DL","DR"]
Coded_Action = ActionCoder(Raw_Action)
Decoded_Action = ActionDecoder(Coded_Action)
print(Raw_Action)
print(Coded_Action)
print(Decoded_Action)
#for coded,decoded in Coded_Action,Decoded_Action:
#    print(coded," --> ",decoded)
"""

def Action_TO_State(currentState,Action):
    #Hareket etseydi nereye giderdi.
    #Expecting action is number
    #Return nextState by decoded (1,2,3,4,5 ... etc)
    
    # Row & Column  (50x50)-->  Decoding   -->  state
    #  decoding      Row 1  -->  1 , 2 , ... , 50
                    #Row 2  -->  51, 52, ... , 100    
    nextState=currentState
    
    
    isGoUp      =   currentState > 50
    isGoDown    =   currentState < ((50*49)+1)
    isGoLeft    =   currentState % 50 != 1
    isGoRight   =   currentState % 50 != 0
    
    isGoUL      =   isGoUp  and  isGoLeft
    isGoUR      =   isGoUp  and  isGoRight
    isGoDL      =   isGoDown and isGoLeft
    isGoDR      =   isGoDown and isGoRight
    
    
    
    
    if(Action == 1  and isGoUp):nextState -= 50 #Up
    if(Action == 2  and isGoDown):nextState += 50 #Down
    if(Action == 3  and isGoLeft):nextState -= 1 #Left
    if(Action == 4 and isGoRight):nextState += 1 #Right
    
    if(Action == 5 and isGoUL):nextState += (-50)+(-1)#UL
    if(Action == 6 and isGoUR):nextState += (-50)+(+1)#UR
    if(Action == 7 and isGoDL):nextState += (50)+(-1)#DL
    if(Action == 8 and isGoDR):nextState += (50)+(+1)#DR
    
    if(nextState == currentState):#Hiçbir işlem yapılmamışsa gidecek yer kalmamıştır.
        print("Action_TO_State içerisinde hiçbir şey yapılmamış:")
        print("currentState:",currentState,"\nAction:",Action)
        return None
    
    return nextState


"""
testing Action_TO_State


print("52,1  Expecting : 2  Real:",end="")
print(Action_TO_State(52,1))

print("52,2  Expecting : 102 Real:",end="")
print(Action_TO_State(52,2))

print("52,3  Expecting : 51  Real:",end="")
print(Action_TO_State(52,3))

print("52,4  Expecting : 53  Real:",end="")
print(Action_TO_State(52,4))

print("52,5  Expecting : 1  Real:",end="")
print(Action_TO_State(52,5))

print("52,6  Expecting : 3  Real:",end="")
print(Action_TO_State(52,6))

print("52,7  Expecting : 101  Real:",end="")
print(Action_TO_State(52,7))

print("52,8  Expecting : 103  Real:",end="")
print(Action_TO_State(52,8))
"""

def available_acs(state,Matrix):
    Acs=[]
    duz=Duz(state,Matrix)
    capraz=Capraz(state,Matrix)
    if(duz is  not None):
        Acs.extend(duz)
    if(capraz is not None):
        Acs.extend(Capraz(state,Matrix))
    
    if(not Acs):
        print("available_acs konuşuyor --> There is no acs")
        return None
    return ActionCoder(Acs)

def available_nextStates(currentState,Actions, Matrix):
    nextStates=[]
    if(Actions is None):
        return None
    
    for action in Actions:
         nextStates.append(Action_TO_State(currentState, action))
            
    return nextStates

def Duz(state,Matrix):
    Acs=[]
    #Yukarı gidebilir mi ? --> Bunun için 50 den büyük olmalı.   
    
    if(state>50):
        tmp_state=Action_TO_State(state, 1)
        R,C=StateToR_C(tmp_state)
        isPassedWay =  Matrix[R][C][1] == "PASSED"
        if(not isPassedWay):
            Acs.append("Up")
    #Aşağı gidebilir mi?
    if(state<(50*49+1)):
        tmp_state=Action_TO_State(state, 2)
        R,C=StateToR_C(tmp_state)
        isPassedWay =  Matrix[R][C][1] == "PASSED"
        if(not isPassedWay):
            Acs.append("Down")
    #sol
    if((state % 50) != 1):
        tmp_state=Action_TO_State(state, 3)
        R,C=StateToR_C(tmp_state)
        isPassedWay =  Matrix[R][C][1] == "PASSED"
        if(not isPassedWay):
            Acs.append("Left")
    #Sağ
    if((state % 50) != 0):
        tmp_state=Action_TO_State(state, 4)
        R,C=StateToR_C(tmp_state)
        isPassedWay =  Matrix[R][C][1] == "PASSED"
        if(not isPassedWay):
            Acs.append("Right")
            
    if(not Acs):
        return None
    return Acs

def Capraz(state,Matrix):
    Acs=[]
    #Action --> boolean expression
    isGoUp      =   state > 50
    isGoDown    =   state < ((50*49)+1)
    isGoLeft    =   state % 50 != 1
    isGoRight   =   state % 50 != 0
    
    isGoUL      =   isGoUp  and  isGoLeft
    isGoUR      =   isGoUp  and  isGoRight
    isGoDL      =   isGoDown and isGoLeft
    isGoDR      =   isGoDown and isGoRight
    

    if(isGoUL):
        tmp_state=Action_TO_State(state, 5)
        R,C=StateToR_C(tmp_state)
        isPassedWay =  Matrix[R][C][1] == "PASSED"
        if(not isPassedWay):
            Acs.append("UL")
    if(isGoUR):
        tmp_state=Action_TO_State(state, 6)
        R,C=StateToR_C(tmp_state)
        isPassedWay =  Matrix[R][C][1] == "PASSED"
        if(not isPassedWay):
            Acs.append("UR")
    if(isGoDL):
        tmp_state=Action_TO_State(state, 7)
        R,C=StateToR_C(tmp_state)
        isPassedWay =  Matrix[R][C][1] == "PASSED"
        if(not isPassedWay):
            Acs.append("DL")
    if(isGoDR):
        tmp_state=Action_TO_State(state, 8)
        R,C=StateToR_C(tmp_state)
        isPassedWay =  Matrix[R][C][1] == "PASSED"
        if(not isPassedWay):
            Acs.append("DR")
    if(not Acs):
        return None
    return Acs
#State controller
def isCrashed(Next_state,Matrix):
    R,C=StateToR_C(Next_state)
    return Matrix[R][C][1] == "RED"       

def isTargetCaptured(Next_state,Matrix):
    R,C=StateToR_C(Next_state)
    
    return Matrix[R][C][1] == "BLUE"

def isPassedWay(Next_state,Matrix):
    R,C=StateToR_C(Next_state)
    return Matrix[R][C][1] == "PASSED"

"""
testing  available_acs -->  Duz,Capraz

import MatrixGenerator50x50 as MAP 
myMap=MAP.MapGenerator(1,1, 49,49,0.2)

ac=available_acs(52,myMap)
avs=available_nextStates(52, ac, myMap)
print("state 52 available actions: ",ac)
print("state 52 available stattes:", avs)

ac=available_acs(1,myMap)
avs=available_nextStates(1, ac, myMap)
print("state 1 available actions: ",ac)
print("state 1 available stattes:", avs)

ac=available_acs(2500,myMap)
avs=available_nextStates(2500, ac, myMap)
print("state 2500 available actions: ",ac)
print("state 2500 available stattes:", avs)
"""
import numpy as np
import random

def selectRandomAction(state,Matrix):
    availableActions = available_acs(state,Matrix)
    if(availableActions is None):
        return None
    
    #randomSelectedAction= availableActions[ np.random.randint( len(availableActions) ) ]
    if(len(availableActions)>0):
        #randomSelectedAction= availableActions[ random.randint( 0,len(availableActions)-1 )]
        if(len(availableActions)!=1):
            randomSelectedAction= availableActions[ np.random.randint( len(availableActions) ) ]
        elif(availableActions is int):
            randomSelectedAction = availableActions
        else:
            print("Gidilecek Yer kalmadı")
            return None
    else:
        print("Gidilecek Yer kalmadı")
        return None
    #selected an action
    randomSelectedState = Action_TO_State(state,randomSelectedAction )
    if(randomSelectedState is None):
        print("randomSelectedState is None\nThere is no action")
        return None
    
    """
    #control nextState deploying this action
    R,C=StateToR_C(randomSelectedState) # WTF
    IsCrashed =isCrashed(state, Matrix)
    IsTargetCapptured = isTargetCaptured(state, Matrix)
    if((not IsCrashed) and (not IsTargetCapptured)):
        #[R][C][1] = "PASSED"
        Matrix[R][C] = (Matrix[R][C][0],"PASSED")
    """
    return randomSelectedAction

def selectGreedyAction(state,Matrix):
    #Available Actions
    availableActions = available_acs(state,Matrix)
    if(availableActions is None):
        return None
    #Rewards of Available Actions
    aARewards=availableActionRewards(availableActions, Matrix)
    #index of Max Reward 

    if(len(aARewards) is not None):
        aARewards_MaxReward_index=np.argmax(aARewards) # Return index of Action
    else:
        print("Seçilebilecek bir seçenek yok")
        return None
        
    
    
    MaxRewardList_element_is_index=[aARewards_MaxReward_index]
    #Birden fazla max değer varsa
    for reward_index in range(len(aARewards)):
        if(aARewards_MaxReward_index != reward_index ):#Kendisi değilse
            if(aARewards[aARewards_MaxReward_index] == aARewards[reward_index]):
                MaxRewardList_element_is_index.append(reward_index)
            
    
    #selecting Greedy Action
    if(len(availableActions) == len(aARewards)):
        if(len(MaxRewardList_element_is_index)==1):
            greedyAction = availableActions[aARewards_MaxReward_index]
        else:
            #1 den fazla max değer için random seçim
            greedyAction_index = MaxRewardList_element_is_index[ np.random.randint(len(MaxRewardList_element_is_index)) ]
            greedyAction = availableActions[greedyAction_index]
    else:
        print("---GreedyAction Available Action listesi ve Onun Ödül listesinin elemanlaı aynı index sırasına sahip değil.")
        greedyAction = None
   
    
    
    
    #greedyAction=greedyAction_index+1 # index starts to count at 0 but action starts to count at 1
    
    
    ## "availableActions"  element index sorting equals to  "aARewards"
    
    #Next state by generated action
    GreedyState = Action_TO_State(state,greedyAction )
    
    #Path üzerinde işaret etmek ve Haritada boyamak için
    #Kontrol et ve işaret et
    """
    R,C=StateToR_C(GreedyState)
    IsCrashed =isCrashed(GreedyState, Matrix)
    IsTargetCapptured = isTargetCaptured(GreedyState, Matrix)
    if((not IsCrashed) and (not IsTargetCapptured)):
        #Matrix[R][C][1] = "PASSED"   Erorr --> 'tuple' object does not support item assignment
        Matrix[R][C] = (Matrix[R][C][0],"PASSED")
    """
    return greedyAction

def selectAction(state,Rate,Matrix):
    random=float(np.random.randint(11)) / 10.0
    
    if(random < Rate):
        selected=selectGreedyAction(state,Matrix)
    else:
        selected=selectRandomAction(state,Matrix)
    
    return selected

#2

def availableActionRewards(availableStates,Matrix):
    if(availableStates is None):
        return None
    
    avsRewards=[]
    for i in range(len(availableStates)):    
        currentAvailableState=availableStates[i]
        R,C=StateToR_C(currentAvailableState)
        avsRewards.append(Matrix[R][C][0])
    return avsRewards

def NextStateAndReward(currentState,Action,Matrix):
    
    
    nextState = Action_TO_State(currentState, Action)

    
    R,C=StateToR_C(currentState)
    reward =  Matrix[R][C][0]
    n_R,n_C=StateToR_C(nextState)
    next_reward=Matrix[n_R][n_C][0]
    
    Walled=isCrashed(nextState, Matrix)
    Captured=isTargetCaptured(nextState, Matrix)
    
    return [nextState,reward,next_reward,Walled,Captured]

"""
testing  selectAction -->  selectRandomAction,selectGreedyAction
         NextStateAndReward --> gerek yok

import MatrixGenerator50x50 as MAP 
myMap=MAP.MapGenerator(1,1, 49,49,0.2)

ac=available_acs(1,myMap)
while not (len(ac)==0): 
    ac=available_acs(1,myMap)
    avs=available_nextStates(1, ac, myMap)
    print("state 1 available actions: ",ac)
    print("state 1 available stattes:", avs)
    avsRewards=[]
    for cs in range(len(avs)):    
        R,C=StateToR_C(cs)
        avsRewards.append(myMap[R][C][0])
    
    
    #Sub selecting function
    print("Rewards: ",avsRewards)
    aRc=selectRandomAction(1, myMap)
    aGc=selectGreedyAction(1, myMap)
    print("RandomSelectedAction Code: ",aRc)
    print("GreedySelectedAction Code: ",aGc)
    print("*"*25)
    
    ac=available_acs(1,myMap)

#Upper Selecting Function
#action=selectAction(2500, 0.5, myMap)
#print("Selected action: ", action)
"""


#Update
def update(Q,current_state, action, learning_rate ,Matrix):
    
    if( (action is None)  or (current_state is None)):
        return None
    
    # Q max (Greedy step)
    availableActions=available_acs(current_state,Matrix)
    if(availableActions is None):
        return Q
    availableNextStates = available_nextStates(current_state,availableActions,Matrix)
    
    #Max q Baslangıçta 0 matris --> update ile değer alır.
    maxQ=MaxRewardFromNextStates(Q,availableNextStates,availableActions)
    
    
    # R
    R,C=StateToR_C(current_state)
    cellType = Matrix[R][C][1] # Buraya BlUE, RED gelebilir.
    reward = Matrix[R][C][0]
    if(cellType == "RED"):
        reward =  -1*reward
    if(cellType == "BLUE"):
        reward =  1000
    #Update Formulle   -1 --> index starts at 0  but  our prams starts at 1
    print("*"*25)
    print("Reward: ",type(reward)," --> ", reward)
    print("MaxQ: ",type(maxQ)," --> ", maxQ)
    print("*"*25)
    print(0<current_state and current_state<=2500  and 0<action and action<=8)
    
    Q[current_state-1,action-1] = (reward) + (learning_rate * maxQ)
    
    return Q



def MaxRewardFromNextStates(Qtable,AvailableStateS,AvailableActionS):
    maxReward = 0
    #maxRewardRow=0
    #maxRewardColumn=0
    for State in AvailableActionS:
        for Action in AvailableActionS:
            reward=Qtable[State-1,Action-1]# -1 olacak  0. index de state 1 var
            #reward=Qtable[State,Action] #bu olmayacak
            if(reward>maxReward):
                maxReward=reward
                
                #maxRewardRow=State
                #maxRewardColumn=Action
    return maxReward


# Train Loop
def Find(sRow,sColumn,tRow,tColumn,RAWMatrix):
    Q = np.matrix(np.zeros([2500,8]))
    LearningRate=0.5
    Matrix =RAWMatrix.copy()
    StartingState = MatrixRowColumnTOstateIDConverter(sRow,sColumn)
    TargetState  = MatrixRowColumnTOstateIDConverter(tRow,tColumn)
    print("StartingState: ",StartingState)
    print("TargetState:",TargetState)
    
    All_Paths=[]
    
    for ep in range(1,50):
        CurrentState = StartingState
        CurrentMatrix=Matrix.copy() # Adımlar işaret bırakacağı için tmp olusturuyoruz.
        pathReward=0
        isTargetCaptured=False
        
        Ep_Path = [StartingState]
        for st in range(1,1000):
            if(CurrentState == TargetState):
                print("Target Captured !!!\nEp: ",ep," Last step: ",st-1)
                isTargetCaptured=True
                break
            
            action = selectAction(CurrentState, 0.5,CurrentMatrix) # Can be BLUE or RED
            if(action is None):
                print("there is No action")
                break
            
            Q=update(Q,CurrentState, action, LearningRate,CurrentMatrix)
            
            nextState,currentReward,next_reward,nextWalled,nextCaptured = NextStateAndReward(CurrentState, action, CurrentMatrix)        
            
            if(nextState == None):
                print("There is no action: NextState: None")
                break
            
            
            if(nextWalled):
                print("Wall !!\n ep: ",ep," Last step: ",st)
                break
            pathReward+=currentReward
            Ep_Path.append(nextState)
            CurrentState=nextState
        All_Paths.append([ep,isTargetCaptured,pathReward,Ep_Path])
        del CurrentMatrix
        
    #print(All_Paths)
    #return Q
    return All_Paths

def test():
    import MatrixGenerator50x50 as MAP 
    myMap=MAP.MapGenerator(1,1, 2,2,0)

    All_Paths = Find(1, 1, 2, 2, myMap)

    optimumPath=[]
    tmp_max_Revard=0
    ID=int()
    #print(All_Paths)

    for ep,isTargetCaptured,pathReward,Ep_Path in All_Paths:
        if(isTargetCaptured):
            if(tmp_max_Revard < pathReward):
                tmp_max_Revard =pathReward
                ID=ep
                optimumPath=Ep_Path
                Leounidas=[ep,isTargetCaptured,pathReward,Ep_Path]
    print("optimumPath:",optimumPath)

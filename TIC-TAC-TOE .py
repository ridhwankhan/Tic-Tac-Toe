 #RIDHWAN KHAN AJAIRA PERA 
#TIC-TAC-TOE game (under construction)
theBoard={ 'top-L':' ' ,'top-M':' ', 'top-R':' ',
           'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
          'low-L':' ',  'low-M':' ', 'low-R':' ',
          }
print(theBoard)
# theBoard[input('input')]='X'
# theBoard[input('input')]='O'

def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])

printBoard(theBoard)
p1=input('PLAYER 1: Please enter your name : ')

p2=input('PLAYER 2: Please enter your name : ')

p1_turn=input('please choose between "X" or "O" : ')

if p1_turn=='X': 
    
    p2_turn='O'
else:
    p2_turn='X'
    
print(f'Player 1 turn is: {p1_turn}')
print(f'Player 2 turn is: {p2_turn}')
draw=0   
 
for turn in range (9):
    if turn%2==0:
        check1=input('PLAYER 1 : please input the position in a format like row-position in caps eg.top-R :')
        # theBoard[input('please input the position in a format like row-position in caps eg.top-R :')] = p1_turn
        while True:
            error=''
            if  check1  in list(theBoard.keys()):
                
                if theBoard[check1]== ' ' :
                    
                    break
                else:
                    error+=f"{check1} is already occupied by {p2}"
                    #checking if the user is trying to overwrite the occupied space 
            else:
                error+='position format not maintained. ' 
            print(f'{error} already occupied wrong move please try again')
            check1=input('PLAYER 1 : please input the position in a format like row-position in caps eg.top-R :')
        
        # if theBoard[check1]==' '
        theBoard[check1] = p1_turn  
        printBoard(theBoard)

        if turn>=4:
            
            if theBoard['top-L']==theBoard['mid-M']==theBoard['low-R']== p1_turn or  theBoard['top-R']==theBoard['mid-M']==theBoard['low-L']== p1_turn or  theBoard['top-L']==theBoard['top-M']==theBoard['top-R']== p1_turn  or  theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R']== p1_turn or  theBoard['low-L']==theBoard['low-M']==theBoard['low-R']== p1_turn  or  theBoard['top-L']==theBoard['mid-L']==theBoard['low-L']== p1_turn  or theBoard['top-M']==theBoard['mid-M']==theBoard['low-M']== p1_turn or theBoard['top-R']==theBoard['mid-R']==theBoard['low-R']== p1_turn :
                
                
                print(f'{p1} WON {p2} LOST')
                draw=1
                
                break
                
        
    else:
        check2=input('PLAYER 2 : please input the position in a format like row-position in caps eg.top-R: ')
        while True:
            error=''
            if  check2  in list(theBoard.keys()):
                
                if theBoard[check2]== ' ' :
                   
                    break
                else:
                    error+=f"{check2} is already occupied by {p1}"
                    
            else:
                error+='Position format not maintained. ' 
            print(f'{error} wrong move please try again')
            check2=input('PLAYER 2 : please input the position in a format like row-position in caps eg.top-R :')
        # else:
        # if theBoard[check2]==' '
        theBoard[check2] = p2_turn
        printBoard(theBoard)
        
        if turn>=4:
            
            if theBoard['top-L']==theBoard['mid-M']==theBoard['low-R']== p2_turn or  theBoard['top-R']==theBoard['mid-M']==theBoard['low-L']== p2_turn or  theBoard['top-L']==theBoard['top-M']==theBoard['top-R']== p2_turn  or  theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R']== p2_turn or  theBoard['low-L']==theBoard['low-M']==theBoard['low-R']== p2_turn  or  theBoard['top-L']==theBoard['mid-L']==theBoard['low-L']== p2_turn  or theBoard['top-M']==theBoard['mid-M']==theBoard['low-M']== p2_turn or theBoard['top-R']==theBoard['mid-R']==theBoard['low-R']== p2_turn :
                
                
                print(f'{p2} WON {p1} lost.') 
                draw=1
                
                break
if draw==0:
    print('MATCH DRAW')      
  
#review ='#' completed '##' 


##need to make a little bit user friendly:::should not enter the values each time. 
##occupied space should not be overwritten by another player 
##show who won   
##Check the loop     
## check 1 e error khacche repeat krle position #solved: check spelling mistake 
# PYGAME  library use  ::: graphic representation needed...   
 
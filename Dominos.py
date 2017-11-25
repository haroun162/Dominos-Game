import random
import collections
#import os
from IPython.display import clear_output
import time

def deckCreation():
""" Create a deck for the game """
    deck=[]
    for i in range (7):
        for j in range (7):
            if (j,i) not in deck:
                couple=(i,j)
                deck.append(couple)
    
    return deck

def getPiece(deck,player):
    if len(deck)==0:
    #the deck is full
        return True
    else:
        player.append(deck.pop()) 

def startHand(deck):
"""Fill the hands of the two players"""
    player=[]
    for i in range (7):
        player.append(deck.pop())
    return player

def emptyHand(palyer):
    if len(player)==0:
        return True
    
def firstPiece(player1,player2):
""" Choose the firt double piece from the two players """
    global turn
    global line
    global line1_firstPiece
    max_val=0
    for piece1 in player1:
        for piece2 in player2:
            
            if piece1[0]==piece1[1] and piece1[0] > max_val:
                max_val=piece1[0]
                ret_piece=piece1
                turn="Player 1"
                
            elif piece2[0]==piece2[1] and piece2[0] > max_val:
                max_val=piece2[0]
                ret_piece=piece2
                turn="Player 2"
                
                
            elif piece1[0]==piece1[1] and piece2[0]==piece2[1] :
                if piece1[0]>piece2[0] and piece1[0]> max_val :
                    max_val=piece1[0]
                    ret_piece=piece1
                    turn="Player 1"
                    
                elif piece2[0]> piece1[0] and piece2[0]> max_val:
                    max_val=piece2[0]
                    ret_piece=piece2
                    turn="Player 2"
                    
                  
    if turn=="Player 1":
        player1.remove(ret_piece)
        turn="Player 2"
        line1_firstPiece = "The first piece was from : you"
        return ret_piece
    else:
        player2.remove(ret_piece)
        turn="Player 1"
        line1_firstPiece = "The first piece was from : the AI"
        return ret_piece
                
def addToLine(piece,line,player,direction):
""" Add pieces to the line with supplementary option to specify the direction 'Left' or 'Right' when two possibilities exist"""
    a,b=piece 
    
    if direction =="":
        direction = "No choice"  # to let access to both if statements
    else:
        direction=direction.upper()
        direction=direction[0]
    
    
    
    if direction == "R" or direction == "No choice":
        if line[-1][1]==a :
            line.append((a,b))
            player.remove(piece)
            return True
        elif line[-1][1]==b :
            line.append((b,a))
            player.remove(piece)
            return True
        
    elif direction == "L" or direction == "No choice":
        if line[0][0]==a :
            line.insert(0,(b,a))
            player.remove(piece)
            return True
        elif line[0][0]==b :
            line.insert(0,(a,b))
            player.remove(piece)
            return True

    else:
        return False


                    
         
def scoreCount(player):
    total=0
    for piece in player:
        total+=(piece[0]+piece[1])
    return total

def aiPlayer(line,ai_hand):
""" A simple algorithme to make the AI play """
    index=0
    max_val=counter=0
    start=line[0][0]
    end=line[-1][1]
    
    for piece in ai_hand:
        index+=1
        a,b=piece
        if a == start or a == end or b == start or b == end:
            if (a+b) >= max_val:
                ret_index=index
                max_val=a+b
    
        else:
            counter+=1
    if counter == len(ai_hand):
        return 0
    else:
        return ret_index
            
def gameBlocked(deck,player1,player2,line):
    #Empty case
    if len(player1)==0 or len(player2)==0 or len(deck)==0 :
        return True
    else:
        return False
    
    # blocked case
    line_num=[]
    start=line[0][0]
    end=line[-1][1]
    
    for piece in line:
        a,b=piece
        line_num.append(a)
        line_num.append(b)
        line_num.sort()
    line_dic=collections.Counter(line_num)
    
    for i in range (len(line_dic)):
        if line_dic[i]==8 and start==i or end==i:
            #The game is blocked
            return True
        else:
            return False

def theWinner():
    global line5_message
    
    line5_message = "*** The game is finished ***"
    
    if scoreCount(ai_hand) > scoreCount(player_hand):
        line5_message += "\n You win "
    else:
        line5_message += "\n You lose "
        
    line5_message += "\n The score of you is : {}".format(scoreCount(player_hand))
    line5_message += "\n The score of the AI is : {}".format(scoreCount(ai_hand))
    
def clc():
    #os.system('CLS')
    clear_output()

def printing ():
    
    global line1_firstPiece 
    global line2_turn
    global line3_line
    global line4_hand       
    global line5_message
    global state_line1
    global line6_state
    
    clc()
    
    print("#"*100)
    
    if state_line1 == 1 or state_line1 == 2:
        #for printing it just once
        print(line1_firstPiece)
        
    else:
        pass
        
    print(line2_turn)
    print(line3_line)
    print(line4_hand)
    print(line6_state)
    print("#"*100)
    print(line5_message)
    print("")
    print("#"*100)


# Variables
line=[]
player_hand=[]
ai_hand=[]
turn=""

line1_firstPiece="" 
line2_turn=""
line3_line=""
line4_hand=""    
line5_message=""
line6_state=""

state_line1=0

#deck
deck=deckCreation()
random.shuffle(deck)

#starting
player_hand=startHand(deck)
ai_hand=startHand(deck)

line.append(firstPiece(player_hand,ai_hand))
        
# Looping
exit_game=False

while exit_game==False and gameBlocked(deck,player_hand,ai_hand,line) == False :

    
    if turn =='Player 1':
        state_line1 +=1 
        done=False
        while done == False:
            
            index=[]
            for i in range (len(player_hand)):
                index.append("{}: {}".format(i+1,player_hand[i]))
            line6_state= "Waiting for your command ..."
            line2_turn = "The turn is for : You "
            line4_hand = "Your hand is :\n\n {} \n".format(index)
            line3_line = "The line is : \n\n {} \n".format(line)
            line5_message += "\n Type the number of the piece or '0' to grab new peace from the deck"
            
            printing ()
            
            
            res = input('')
            try:
                ans,direction = res.split(' ')
                ans = int(ans)
            except ValueError:
                ans,direction = res,""
                ans = int(ans)
            
            
            while ans == 0:
                true_if_empty_deck=getPiece(deck,player_hand)
                line5_message += "\n\t You grabed a new piece from the deck"
                
                index=[]
                for i in range (len(player_hand)):
                    index.append("{}: {}".format(i+1,player_hand[i]))
                line4_hand = "Your hand is :\n\n {} \n".format(index)
                
                printing ()
                
                res = input('')
                try:
                    ans,direction = res.split(' ')
                    ans = int(ans)
                except ValueError:
                    ans,direction = res,""
                ans = int(ans)
                
                if true_if_empty_deck==True:
                    exit_game=True

            
            while True:
                try:
                    piece=player_hand[ans-1]

                    break
                except IndexError:
                    
                    line5_message += "\n\t Enter a good value ! or type '0' to get new piece"
                    printing ()
                    
                    res = input('')
                    try:
                        ans,direction = res.split(' ')
                        ans = int(ans)
                    except ValueError:
                        ans,direction = res,""
                        ans = int(ans)
                    

            chosen_piece = player_hand[ans-1]
            done=addToLine(chosen_piece,line,player_hand,direction)
                
            if done:
                turn='Player 2'
                line5_message += "\n You played : {}".format(chosen_piece)

    if turn =='Player 2' :
        state_line1 +=1 
        done=False
        while done == False:
            line6_state= "The AI is playing ..."
            line2_turn = "The turn is for : the AI"
            
            ans_ai=aiPlayer(line,ai_hand)
            
            line3_line = "The line is : \n\n {}".format(line)
            
            printing ()
            time.sleep(3)
            
            if ans_ai == 0:
                empty_deck=getPiece(deck,ai_hand)
                
                line3_line = "The line is : \n\n {}".format(line)
                line5_message +="\n\t A piece has been taken from the deck"
                
                printing ()
                time.sleep(2)
                
                if empty_deck==True:
                    exit_game=True
                    
            chosen_piece = ai_hand[ans_ai-1]
            empty_string=""
            done=addToLine(chosen_piece,line,ai_hand,empty_string)
            if done:
                line6_state= ""
                line5_message += "\n THE AI HAS PLAYED : {}".format(chosen_piece)
                turn='Player 1'
                printing ()
    

theWinner()
    

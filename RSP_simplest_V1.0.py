from random import randint
import time
from os import system


print("----------------------------------------------------------------------------------")
print("Let's play Rock - scissors - paper Version 1")
print("0    -   ROCK")
print("1    -   SCISSORS")
print("2    -   PAPER")
print("Q/q    -   QUIT")
print("----------------------------------------------------------------------------------")
count=1
bot_score=0
player_score=0

while True:
    _ = system('cls') 
    print("GAME N "+ str(count) + "  |  RESULT: MACHINE " + str(bot_score) + " - PLAYER "+str(player_score))
    bot_move=randint(0, 2)
    player_move = str(input("SHOOT: "))
    if player_move != '0' and player_move!= '1' and player_move!= '2' and player_move!= 'Q' and player_move!= 'q':
        print("WHAAATTT, COME ON, YOU ARE THE INTELLIGENT, YOU SHOULD WRITE JUST ONE OF THIS CHARACTERS 0-1-2-Q-q")
        time.sleep(3) # Sleep for 3 seconds
        continue
    else:
        if player_move == 'Q' or player_move == 'q':
            if bot_score>player_score:
                print("GOOD BYE LOOOSER")
                time.sleep(1) 
                print("L")
                time.sleep(1) 
                print("O")
                time.sleep(1)
                print("S")
                time.sleep(1)
                print("E")
                time.sleep(1)
                print("R")
            else:
                print("GOOD BYE MASTER!")
            time.sleep(1)
            _ = system('cls') 
            break

    player_move=int(player_move)


    if player_move==0:
        print("YOU: ROCK")
    elif player_move==1:
        print("YOU: SCISSORS")
    elif player_move==2:
        print("YOU: PAPER")

    if bot_move==0:
        print("ME: ROCK")
    elif bot_move==1:
        print("ME: SCISSORS")
    elif bot_move==2:
        print("ME: PAPER")
    time.sleep(2)
    
    if player_move == bot_move:
        print("TECHNICAL DRAW")
    elif (player_move == 0 and bot_move==1):
        print("THIS POINT IS YOURS MASTER")
        player_score=player_score+1
    elif (player_move == 1 and bot_move==2):
        print("THIS POINT IS YOURS MASTER")
        player_score=player_score+1
    elif (player_move== 2 and bot_move==0):
        print("THIS POINT IS YOURS MASTER")
        player_score=player_score+1
    else: 
        print("THIS POINT IS MINE, IN YOUR FACE!!!!")
        bot_score=bot_score+1

     
    time.sleep(2)
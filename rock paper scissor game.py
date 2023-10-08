#TASK 2 ROCK PAPER AND SCISSOR GAME
#codsoft#@codsoft#codsoftintership
import random
a=["rock","paper","scissor"];
'''rock v/s scissor-->rock wins
   rock v/s paper-->paper wins
   paper v/s scissor-->scissor wins'''
while True:
    ucount=0;
    ccount=0;
    uc=int(input('''GAME START:
                                    Press 1-->yes
                                    press 2-->no|exit'''));
    if uc==1:
        for i in range(1,6):
            userinput=int(input('''
                                   press 1-->rock
                                   press 2-->paper
                                   press 3-->scissor'''));
            Uchoice=0;
            if userinput==1:
                Uchoice="rock";
            elif userinput==2:
                Uchoice="paper";
            elif userinput==3:
                Uchoice="scissor";
            else:
                print("invalid choice");
            compin=random.choice(a);
            print("user choice",Uchoice);
            print("computer choice",compin);
            if Uchoice==compin:
                print("user choice",Uchoice);
                print("computer choice",compin);
                print("GAME OVER");
                ccount=ccount+1;
                ucount=ucount+1;
            elif Uchoice=="rock" and compin=="scissor" or Uchoice=="paper" and compin=="rock" or Uchoice=="scissor" and compin=="paper":
                print("computer choice",compin);
                print("user choice",Uchoice);
                print("YOU WIN");
                ucount=ucount+1;
            else:
                print("computer choice",compin);
                print("user choice",Uchoice);
                print("COMPUTER WIN");
                ccount=ccount+1;
        if ucount==ccount:
                print("user score",ucount);
                print("computer score",ccount);
                print("SERIES DRAW");
        elif ucount>ccount:
                print("user score",ucount);
                print("computer score",ccount);
                print("YOU WIN THE SERIES");
        else:
                print("user score",ucount);
                print("computer score",ccount);
                print("COMPUTER WIN THE SERIES");
        

    else:
        break;
    

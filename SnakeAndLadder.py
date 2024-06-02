from tabnanny import check
from PIL import Image
import random

end = 100

def show_board():
    img = Image.open("board.jpg")
    img.show()

def check_ladder(points):
    if points == 2:    
        return 23 #and True
    elif points == 8:        
        return 12 #and True
    elif points == 17:
        return 93 #and True
    elif points == 29:
        return 54 #and True
    elif points == 32:
        return 51 #and True
    elif points == 39:
        return 80 #and True
    elif points == 62:
        return 78 #and True
    elif points == 70:
        return 89 #and True
    elif points == 75:
        return 96 #and True
    else:
        return points #and False

def check_snake(points):
    if points == 31:
        print("Snake")
        return 14
    elif points == 41:
        print("Snake")
        return 20
    elif points == 59:
        print("Snake")
        return 37
    elif points == 67:
        print("Snake")
        return 50
    elif points == 83:
        print("Snake")
        return 80
    elif points == 92:
        print("Snake")
        return 76
    elif points == 99:
        print("Snake")
        return 4
    else:
        return points

def reached_end(points):
    if points == end:
        return True
    else:
        False

def play():
    # input player 1 name
    p1_name = input("Player 1, Please Enter your Name: ")
    # input player 2 name
    p2_name = input("Player 2, Please Enter your Name: ")

    # initial points of player 1
    p1_points = 0
    # initial points of player 1
    p2_points = 0

    turn = 0

    while(1):
        if turn%2 == 0:
            # player 1 turn
            print(p1_name," your turn.")
            # ask players choice to continue
            c = int(input("Press 1 to Continue, 0 to Quit: "))
            if c==0:
                print(p1_name, " scored ", p1_points)
                print(p2_name, " scored ", p2_points)
                print("Quitting The Game!!!, Thanks For Playing!!")
                break
            # generate a random number from 1 to 6
            while True:
                dice = random.randint(1,6)
                print("Dice Showed: ",dice)
                p1_points += dice
                check1 = p1_points
                p1_points = check_ladder(p1_points)
                if(p1_points==check1):
                    p1_points = check_snake(p1_points)
                    break
                else:
                    print("You Got Ladder!!!!!")
                    print("You are at: ",p1_points)
                    print("You Got One More Turn.")
                    continue
            if p1_points > end:
                print("You need ",(end - p1_points)," to Win.")
            
            print(p1_name,"You are at: ",p1_points)

            if reached_end(p1_points):
                print(p1_name, " You Won The Game!!!!!")
                break

        else:
            # player 2 turn
            print(p2_name," your turn.")
            # ask players choice to continue
            c = input("Press 1 to Continue, 0 to Quit: ")
            if c=="0":
                print(p1_name, " scored ", p1_points)
                print(p2_name, " scored ", p2_points)
                print("Quitting The Game!!!, Thanks For Playing!!")
                break
            # generate a random number from 1 to 6
            while True:
                dice = random.randint(1,6)
                print("Dice Showed: ",dice)
                p2_points += dice
                check2 = p2_points
                p2_points = check_ladder(p2_points)
                if(p2_points==check2):
                    p2_points = check_snake(p2_points)
                    break
                else:
                    print("You Got Ladder!!!!!")
                    print("You are at: ",p2_points)
                    print("You Got One More Turn.")
                    continue

            if p2_points > end:
                print("You need ",(end - p2_points)," to Win.")

            print(p2_name,"You are at: ",p2_points)

            if reached_end(p2_points):
                print(p2_name, " You Won The Game!!!!!")
                break

        turn += 1
show_board()
play()
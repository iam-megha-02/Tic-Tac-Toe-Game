
import numpy as np
game_board = np.zeros((3,3))

#Define the players

player_1 = input("Enter the name of player 1: ")
player_2 = input("Enter the name of player 2: ")


turns = 0
while turns <= 9:

    for trn in range(1,10):
        if not trn%2 == 0:
            player = player_1
            print("It is",player,"turn!")
            row = int(input("Enter the row you want to fill: "))
            column = int(input("Enter the column you want to fill: "))

            if game_board[row][column] == 1 or game_board[row][column] == 2:
                print("Choose another block!")
                row = int(input("Enter the row you want to fill: "))
                column = int(input("Enter the column you want to fill: "))
                game_board[row][column] = 1
                print(game_board)
            
            else:

                if game_board[row][column] == 0:
                    game_board[row][column] = 1
                    print(game_board)
        else:
            player = player_2
            print("It is",player,"turn!")
            row = int(input("Enter the row you want to fill: "))
            column = int(input("Enter the column you want to fill: "))

            if game_board[row][column] == 1 or game_board[row][column] == 2:
                print("Choose another block!")
                row = int(input("Enter the row you want to fill: "))
                column = int(input("Enter the column you want to fill: "))
                game_board[row][column] = 2
                print(game_board)
            else:
                if game_board[row][column] == 0:
                    game_board[row][column] = 2
                    print(game_board)
                

    #--------COMBINATIONS--------
        

        if (game_board[0][0] == 1 and game_board[0][1] == 1 and game_board[0][2] == 1 ) or ( game_board[1][0] == 1 and game_board[1][1] == 1 and game_board[1][2] == 1) or ( game_board[2][0] == 1 and game_board[2][1] == 1 and game_board[2][2] == 1) \
        or ( game_board[0][0] == 1 and game_board[1][0] == 1 and game_board[2][0] == 1) or ( game_board[0][1] == 1 and game_board[1][1] == 1 and game_board[2][1] == 1) or ( game_board[0][2] == 1 and game_board[1][2] == 1 and game_board[2][2] == 1) \
        or ( game_board[0][2] == 1 and game_board[1][1] == 1 and game_board[2][0] == 1) or ( game_board[0][0] == 1 and game_board[1][1] == 1 and game_board[2][2] == 1):
            print(player_1,"Wins!")
            exit()
            

        if (game_board[0][0] == 2 and game_board[0][1] == 2 and game_board[0][2] == 2 ) or ( game_board[1][0] == 2 and game_board[1][1] == 2 and game_board[1][2] == 2) or ( game_board[2][0] == 2 and game_board[2][1] == 2 and game_board[2][2] == 2) \
        or ( game_board[0][0] == 2 and game_board[1][0] == 2 and game_board[2][0] == 2) or ( game_board[0][1] == 2 and game_board[1][1] == 2 and game_board[2][1] == 2) or ( game_board[0][2] == 2 and game_board[1][2] == 2 and game_board[2][2] == 2) \
        or ( game_board[0][2] == 2 and game_board[1][1] == 2 and game_board[2][0] == 2) or ( game_board[0][0] == 2 and game_board[1][1] == 2 and game_board[2][2] == 2):
            print(player_2,"Wins!")
            exit()

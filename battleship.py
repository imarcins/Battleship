def x_y(aim):
 
 
  x = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
 
  }
 
  y = {
    "1" : 0,
    "2" : 1,
    "3" : 2,
    "4" : 3,
    "5" : 4,
  }
  try:
    return x[aim[0]], y[aim[1]]
  except: 
    return False
 

def print_board(board):
    print("1 2 3 4 5")
    for x in board:
        
        print(*x)
    
def board_presentation():
    print("Player 1 board")
    print_board(player1_board)
    print("=============")
    print("Player 2 board")
    print_board(player2_board)

level_length = 5
player1_board = [["-" for _ in range(level_length)] for _ in range(level_length)]
player2_board = [["-" for _ in range(level_length)] for _ in range(level_length)]

player1_ships = [["-" for _ in range(level_length)] for _ in range(level_length)]
player2_ships = [["-" for _ in range(level_length)] for _ in range(level_length)]
 
def ship_placement(player_ships, x_y):
    x,y = x_y
    if player_ships[x][y] == "S":
        print("This spot is taken")
        return False
    else: 
        player_ships[x][y] = "S"
        print("Placed ship")
        return True
    




def placement_turns(player_ships):
    ships = 1
    while ships <= 3:
        board_presentation()
        choice = x_y(input("Please place 3 ships (1x1): ").upper())
        if choice:
            if ship_placement(player_ships, choice):
                ships += 1 
        else: 
            print("Invalid coordinates")

def look_for_ship(player_ships):
    for item in player_ships:
        if "S" in item: 
            return True
            
        else: 
            return False 
def shooting(player_board, player_ships, x_y):
    x,y = x_y

    
    if player_ships[x][y] == "S":
        player_board[x][y] = "X"
        player_ships[x][y] = "-"
        print("You sunk the target, good job!")
    elif player_board[x][y] == "X" or "O":
        print("You have already shot at this spot!")

        return True
    else: 
        print("You missed")
        player_board[x][y] = "O"
        return False
def main():
    print("Player 1 Turn")
    print("========")
    placement_turns(player1_ships)
    print("Player 2 Turn")
    print("========")
    placement_turns(player2_ships)
    print("Start shooting")
    while look_for_ship(player1_ships) and look_for_ship(player2_ships):
        board_presentation()

        shooting(player1_board, player2_ships, x_y(input("Player two Please choose where you want to shoot: ").upper()))
        board_presentation()

        shooting(player2_board, player1_ships, x_y(input("Player one please choose where you want to shoot: ").upper()))
        
    else:
        if look_for_ship(player1_ships) == False: 
            print("Player 2 wins")
            
        else:
            print("Player 1 wins")
            





    


main()



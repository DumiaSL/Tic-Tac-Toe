
def print_grid(value_list):
            "This is a function for print the grid"
            for row in value_list:
                print("-------------")
                print("| ", end="")
                print(*row, sep=(" | "), end="")
                print(" |")
            print("-------------")


def exit_game(player_num):
        "This is a function for exit the game"
        if player_num.lower() == "e":
            print('''Thank you for playing
Hope you enjoyed this game''')
            return True
        else:
            return False



def check_num(player_num):
        "This is a function for check input numbers of players "
        # check if its a number
        if not isnum(player_num):
            return False
        player_num = int(player_num)
        # check if its 1 - 9
        if not valid(player_num):
            return False

        return True

def isnum(player_num):
        "This is a function for checking if it is number or not"
        if not player_num.isnumeric():
            print("This is not a valid number")
            return False
        else:
            return True

def valid(player_num):
        "This is a function for checking if it is in the bounds 1 to 9"
        if player_num > 9 or player_num < 1:
            print("This is out of range")
            return False
        else:
            return True            

def check_diag(user,value_list):
            # top left to bottom right
        if value_list[0][0] == user and value_list[1][1] == user and value_list[2][2] == user:
            return True
        elif value_list[0][2] == user and value_list[1][1] == user and value_list[2][0] == user:
            return True
        else:
            return False

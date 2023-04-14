import mysql.connector
from mysql.connector import Error
from datetime import datetime
import sub.second

# tic tac toe

#define variables
print('tic tac toe game')
print()
print()

#Check database connection
try:
    db = mysql.connector.connect (host='localhost',user ='root',password='',database ="db_tic_tac")
    if db.is_connected():

        again = "yes"
        while again == "yes":

            #Open database connection
            db = mysql.connector.connect (host='localhost',user ='root',password='',database ="db_tic_tac")
            #Prepare a cursor object using cursor() method
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(rec_num) FROM mytable")
            data = cursor.fetchall()
            for item in data:
                    for i in item:
                        rec_count = int(i)
            if int(rec_count) == 0:
                rec_num =1
            else:
                cursor.execute("SELECT MAX(rec_num) FROM mytable")
                data = cursor.fetchall()
                #calling last record number
                for item in data:
                    for i in item:
                        rec_num = int(i) + 1

            insertnum = "insert into mytable(rec_num) values("+str(rec_num)+") "
            cursor.execute(insertnum)

            #calling the date and time
            now = datetime.now()
            day = now.strftime("%m/%d/%Y\t%H:%M:%S")
            print(day)
            update_date = "update mytable set date_and_time ='"+str(day)+"'where rec_num ="+str(rec_num)+""
            cursor.execute(update_date)
            print()

            

        #--------Input players----------------------
            player_1=input("Enter player name_1: ")
            while True:
                record1 =input("Do you want to see pass records[YES/NO]: ").upper()
                if record1=="YES":
                    cursor.execute("SELECT COUNT(rec_num) FROM mytable ;")
                    data = cursor.fetchall()
                    for item in data:
                            for i in item:
                                tot_count = int(i)
                    cursor.execute("SELECT COUNT(winner) FROM mytable WHERE winner='Match tied' ;")
                    data = cursor.fetchall()
                    for item in data:
                            for i in item:
                                drw_count = int(i)
                    
                    print("========================================               ============================= ")
                    print("	Total games play -",tot_count,"                               ",
                    "Total draws -",drw_count )
                    print("========================================               =============================")
                    print()
                    print()
                    print("====================================================================================================================================================================================")
                    print(f"|{'rec_num' : ^35}|{'date_and_time' : ^35}|{'player_1' : ^35}|{'player_2' : ^35}|{'winner' : ^35}|")
                    print("====================================================================================================================================================================================")
                    cursor.execute("SELECT * FROM mytable WHERE (player_1='"+player_1+"'or player_2='"+player_1+"')")
                    data = cursor.fetchall()
                    for item in data:
                        print("|",end="")
                        for i in item:
                            if i is None:
                                print(f"{'' : ^35}",end='|')
                            else:
                                print(f"{i : ^35}",end='|')
                        print()
                        
                    print("====================================================================================================================================================================================")
                    print()
                    print()
                    cursor.execute("SELECT COUNT(player_1) FROM mytable WHERE (player_1='"+player_1+"') AND (winner='"+player_1+"');")
                    data = cursor.fetchall()
                    for item in data:
                            for i in item:
                                rec_count = int(i)
                    print("=====================================")
                    print("	Total wins by " +player_1+"-",rec_count,"")
                    print("=====================================")
                    print()

                    
                        
                   
                    print()
                    break
                elif record1=="NO":
                    break
                else:
                    print("Invalid answer")

            player_2=input("Enter player name_2: ")
            while True:
                record1 =input("Do you want to see pass records[YES/NO]: ").upper()
                if record1=="YES":
                    cursor.execute("SELECT COUNT(rec_num) FROM mytable ;")
                    data = cursor.fetchall()
                    for item in data:
                            for i in item:
                                tot_count = int(i)
                    cursor.execute("SELECT COUNT(winner) FROM mytable WHERE winner='Match tied' ;")
                    data = cursor.fetchall()
                    for item in data:
                            for i in item:
                                drw_count = int(i)
                    
                    print("========================================               ============================= ")
                    print("	Total games play -",tot_count,"                               ",
                    "Total draws -",drw_count )
                    print("========================================               =============================")
                    print()
                    print()

                    print("====================================================================================================================================================================================")
                    print(f"|{'rec_num' : ^35}|{'date_and_time' : ^35}|{'player_1' : ^35}|{'player_2' : ^35}|{'winner' : ^35}|")
                    print("====================================================================================================================================================================================")
                    cursor.execute("SELECT * FROM mytable WHERE (player_1='"+player_2+"'or player_2='"+player_2+"')")
                    data = cursor.fetchall()
                    for item in data:
                        print("|",end="")
                        for i in item:
                            if i is None:
                                print(f"{'' : ^35}",end='|')
                            else:
                                print(f"{i : ^35}",end='|')
                        print()
                        
                    print("====================================================================================================================================================================================")
                    print()
                    print()
                    cursor.execute("SELECT COUNT(player_2) FROM mytable WHERE (player_2='"+player_2+"') AND (winner='"+player_2+"');")
                    data = cursor.fetchall()
                    for item in data:
                            for i in item:
                                rec_count = int(i)
                                
                            
                    print("=====================================")
                    print("	Total wins by " +player_2+"-",rec_count,"")
                    print("=====================================")
                    print()

                    
                    break
                elif record1=="NO":
                    break
                else:
                    print("Invalid answer")


            #calling player_1_name
            player_1_name ="update mytable set player_1 ='"+str(player_1)+"'where rec_num ="+str(rec_num)+""
            cursor.execute(player_1_name)

            #calling player_1_name
            player_2_name ="update mytable set player_2 ='"+str(player_2)+"'where rec_num ="+str(rec_num)+""
            cursor.execute(player_2_name)


            value_list = [
                    ["-", "-", "-"],
                    ["-", "-", "-"],
                    ["-", "-", "-"]
                ]

            user = True  # when true it refers to x, otherwise o
            turns = 0



            def istaken(coords, value_list):
                    row = coords[0]
                    col = coords[1]
                    if value_list[row][col] != "-":
                        print("This position is already taken.")
                        return True
                    else:
                        return False


            def coordinates(player_num):
                    row = int(player_num / 3)
                    col = player_num
                    if col > 2:
                        col = int(col % 3)
                    return (row, col)


            def add_to_board(coords, value_list, active_user):
                    row = coords[0]
                    col = coords[1]
                    value_list[row][col] = active_user


            def current_user(user):
                    if user:
                        return "x"
                    else:
                        return "o"


            def iswin(user, value_list):
                    if check_row(user, value_list):
                        return True
                    if check_col(user,value_list):
                        return True
                    if sub.second.check_diag(user, value_list):
                        return True
                    return False


            def check_row(user, value_list):
                    for row in value_list:
                        complete_row = True
                        for slot in row:
                            if slot != user:
                                complete_row = False
                                break
                        if complete_row:
                            return True
                    return False


            def check_col(user, value_list):
                    for col in range(3):
                        complete_col = True
                        for row in range(3):
                            if value_list[row][col] != user:
                                complete_col = False
                                break
                        if complete_col:
                            return True
                    return False




                #-----------------------------------Main program-------------------------------------------------
            while turns < 9:
                    active_user = current_user(user)
                    
                    sub.second.print_grid(value_list)
                    if active_user=="x":
                        player_num = input(player_1 +
                        " Please enter a number between 1 to 9 or 'e' to exit the game: ")
                    else:
                        player_num = input(player_2 +
                        "  Please enter a number between 1 to 9 or 'e' to exit the game: ")
                    if sub.second.exit_game(player_num):
                        break
                    if not sub.second.check_num(player_num):
                        print("Please try again.")
                        continue
                    player_num = int(player_num) - 1
                    coords = coordinates(player_num)
                    if istaken(coords, value_list):
                        print("Please try again.")
                        continue
                    add_to_board(coords, value_list, active_user)
                    if iswin(active_user, value_list):
                        sub.second.print_grid(value_list)
                        if active_user=="x":
                            player_1_name ="update mytable set winner ='"+str(player_1)+"'where rec_num ="+str(rec_num)+""
                            cursor.execute(player_1_name)
                
                            print("Congratulations",player_1, ",you won the game!")
                        else:
                            player_2_name ="update mytable set winner ='"+str(player_2)+"'where rec_num ="+str(rec_num)+""
                            cursor.execute(player_2_name)
                            print("Congratulations",player_2, ",you won the game!")
                        break
 
                    
                    turns += 1
                    if turns == 9:
                        tie ="update mytable set winner ='"+"Match tied"+"'where rec_num ="+str(rec_num)+""
                        cursor.execute(tie)
                        sub.second.print_grid(value_list)
                        print("Tie!")
                    user = not user

            db.commit()
            db.close()
            again = input("Do you want to play again this game: ").lower()
            print()
            print('''Thank you for playing
Hope you enjoyed this game''')
except Error as e:
    print("Oops!")
    print(e)

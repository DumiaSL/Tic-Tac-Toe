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

            

        

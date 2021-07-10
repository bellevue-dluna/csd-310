# Denae Luna
# CSD-310
# Module 9.2

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database User {} connected to MySQL on host {} with database {}\n\n".format(config["user"], config["host"], config["database"]))

except mysql.connector.Error as err:
    if err.errno == errorcode.errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or passwork is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

# Performs table queries
sql_join_query = "\
    SELECT player_id, first_name, last_name, team_name\
        FROM player\
         INNER JOIN team\
             ON player.team_id = team.team_id"

cursor = db.cursor()

# executes team query and prints results
cursor.execute(sql_join_query)
players = cursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}\n".format(player[3]))

db.close()

input("\n\n Press any key to contine...")
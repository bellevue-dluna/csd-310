# Denae Luna
# CSD-310
# 04 July 2021

import mysql.connector
from mysql.connector import errorcode

# creates object for database access
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# tries to connect to database
try:
    db = mysql.connector.connect(**config)

    print("\n Database User {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or passwork is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

# Performs table queries
sql_team_query = "SELECT team_id, team_name, mascot FROM team"
sql_player_query = "SELECT player_id, first_name, last_name, team_id FROM player"

cursor = db.cursor()

# executes team query and prints results
cursor.execute(sql_team_query)
teams = cursor.fetchall()

print("-- DISPLAYING TEAM RECORDS --")
for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot: {}\n".format(team[2]))

# executes player query and prints results
cursor.execute(sql_player_query)
players = cursor.fetchall()

print("\n-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}\n".format(player[3]))
db.close()
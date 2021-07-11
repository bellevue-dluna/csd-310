# Denae Luna
# CSD-310
# Module 9.3

from dns.rdatatype import NULL
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

#function to print players
def print_players(players):
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}\n".format(player[3]))

def insert_SQL(cursor, query, vals):
    cursor.execute(query, vals)
    db.commit()

def read_SQL(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

def update_SQL(cursor, query):
    cursor.execute(query)
    db.commit()

# holds query strings
sql_join_query = "\
    SELECT\
        player_id,\
        first_name,\
        last_name, team_name\
    FROM player\
      INNER JOIN team\
        ON player.team_id = team.team_id\
    ORDER BY player_id"

sql_insert_query = "\
    INSERT INTO\
        player(player_id,\
        first_name,\
        last_name,\
        team_id)\
    VALUES (%s,%s,%s,1)"

sql_update_query = "\
    UPDATE player\
    SET team_id = 2\
    WHERE player_id = 7"

sql_delete_query ="\
    DELETE FROM player\
    WHERE player_id = 7"

new_player = [7, 'Harry', 'Potter']
cursor = db.cursor()

# executes INSERT query
insert_SQL(cursor, sql_insert_query, new_player)

# executes JOIN query
players = read_SQL(cursor, sql_join_query)

#prints list of players
print("-- PLAYERS AFTER INSERT --")
print_players(players)

# executes UPDATE query
update_SQL(cursor, sql_update_query)

# rereads table
players = read_SQL(cursor, sql_join_query)

#prints list of players
print("-- PLAYERS AFTER UPDATE --")
print_players(players)

# executes DELETE query
cursor.execute(sql_delete_query)
db.commit()

# rereads table
players = read_SQL(cursor, sql_join_query)

#prints list of players
print("-- PLAYERS AFTER DELETE --")
print_players(players)

db.close()
input("\n\nPress any key to continue...")
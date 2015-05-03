## tournament.py -- implementation of a Swiss-system tournament.


import psycopg2


def close_cursor_and_connection(cursor, connection):  # Close cursor and connection objects.
    cursor.close()
    connection.close()


def get_cursor_and_connection():  # Returns connection and cursor objects.
    connection = connect()
    return connection, connection.cursor()


def connect():  # Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect("dbname=tournament")


def delete_matches():  # Remove all the match records from the database.
    connection, cursor = get_cursor_and_connection()
    cursor.execute("DELETE FROM Matches;")
    connection.commit()
    close_cursor_and_connection(cursor, connection)


def delete_athletes():  # Remove all the athletes records from the database.
    connection, cursor = get_cursor_and_connection()
    cursor.execute("DELETE FROM Athletes;")
    connection.commit()
    close_cursor_and_connection(cursor, connection)


def count_athletes():  # Returns the number of athletes currently registered.
    connection, cursor = get_cursor_and_connection()
    cursor.execute("SELECT COUNT(AthleteID) FROM Athletes;")
    count_of_athletes = cursor.fetchone()[0]
    close_cursor_and_connection(cursor, connection)

    return count_of_athletes


def register_athlete(name):  # Adds an athlete to the tournament database.
    connection, cursor = get_cursor_and_connection()
    cursor.execute("INSERT INTO Athletes (Name) VALUES(%s)", (name,))
    connection.commit()
    close_cursor_and_connection(cursor, connection)


def athlete_standings():  #Returns a list of the athletes and their win records, sorted by wins.
    """The first entry in the list should be the athlete in first place, or an athlete tied for first place if there is currently a tie.
    Returns: A list of tuples, each of which contains (id, name, wins, matches):
            id: the athlete's unique id (assigned by the database)
            name: the athlete's full name (as registered)
            wins: the number of matches the athlete has won
            matches: the number of matches the athlete has fought."""
    query = """SELECT Win.AthleteID, Win.Name,
                COALESCE(Win."WinCount", 0),
                COALESCE(Mat."MatchCount", 0)
                FROM
                    (
                    SELECT Athl.AthleteID, Athl.Name,
                    COALESCE(wincount, 0) as "WinCount"
                    FROM Athletes Athl
                    LEFT JOIN (
                        SELECT Mat.AthleteID, COUNT(Mat.Result) as wincount
                        FROM Matches Mat
                        WHERE Mat.Result = 'Win'
                        GROUP By Mat.AthleteID
                        ) WC
                    ON Athl.AthleteID=WC.AthleteID
                    ) Win
                LEFT JOIN
                    (
                    SELECT Mat.AthleteID,
                    COALESCE(COUNT(Mat.Result), 0) as "MatchCount"
                    FROM Matches Mat
                    GROUP BY Mat.AthleteID
                    ) Mat
                    
                ON Win.AthleteID=Mat.AthleteID
                ORDER By COALESCE(Win."WinCount", 0) Desc;"""

    connection, cursor = get_cursor_and_connection()
    cursor.execute(query) 
    results = cursor.fetchall()
    close_cursor_and_connection(cursor, connection)

    return results

def report_match(winner, loser):  # Records the outcome of a single match between two athletes.
    """ Args:
      winner:  the id number of the Athlete who won
      loser:  the id number of the Athlete who lost """

    connection, cursor = get_cursor_and_connection()
    cursor.execute("INSERT INTO Matches VALUES(%s, %s)", (winner, 'Win'))
    cursor.execute("INSERT INTO Matches VALUES(%s, %s)", (loser, 'Loss'))
    connection.commit()
    close_cursor_and_connection(cursor, connection)
 
 
def swiss_pairings():
    """ Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of athletes registered, each athlete appears exactly once in the pairings.
    Each athlete is paired with another athlete with an equal or nearly-equal win record, that is, an athlete adjacent to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: The first athlete's unique id.
        name1: The first athlete's name.
        id2: The second athlete's unique id.
        name2: The second athlete's name. """

    standings = athlete_standings()

    pairings = []
    paired = []
    for athlete in standings:
        # if len < 4, less than 2 players are paired each athlete has a len of 2 because id and name are used for each athlete.
        if len(paired) < 4:
            paired.append(athlete[0])
            paired.append(athlete[1])
        # if len == 4, 2 athletes are paired.
        if len(paired) == 4:
            pairings.append(tuple(paired))
            paired = []

    return pairings

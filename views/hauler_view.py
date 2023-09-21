import sqlite3
import json

def list_haulers():
    # Open a connection to the database
    with sqlite3.connect("./shipping.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            h.id,
            h.name,
            h.dock_id
        FROM Hauler h
        """)
        query_results = db_cursor.fetchall()

        # Initialize an empty list and then add each dictionary to it
        haulers=[]
        for row in query_results:
            haulers.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_haulers = json.dumps(haulers)

    return serialized_haulers

def retrieve_hauler(pk):
    # Open a connection to the database
    with sqlite3.connect("./shipping.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            h.id,
            h.name,
            h.dock_id
        FROM Hauler h
        WHERE h.id = ?
        """, (pk,))
        query_results = db_cursor.fetchone()

        # Serialize Python list to JSON encoded string
        serialized_hauler = json.dumps(dict(query_results))

    return serialized_hauler

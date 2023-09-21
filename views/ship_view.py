import sqlite3
import json
from nss_handler import status

class ShippingShipsView():

    def get(self, handler, url):
        with sqlite3.connect("./shipping.db") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            if url["pk"] != 0:
                db_cursor.execute(""" SELECT s.id, s.name, s.hauler_id FROM Ship s WHERE s.id = ? """, (url["pk"],))
                query_results = db_cursor.fetchone()
                serialized_ship = json.dumps(dict(query_results))

                return handler.send_response(serialized_ship, status.SUCCESS_200.value)

            db_cursor.execute(""" SELECT s.id, s.name, s.hauler_id FROM Ship s """)
            query_results = db_cursor.fetchall()
            ships=[dict(row) for row in query_results]
            serialized_ships = json.dumps(ships)

            return handler.response(serialized_ships, status.SUCCESS_200.value)


from contextlib import contextmanager

import psycopg2
from psycopg2.pool import ThreadedConnectionPool
    

class DBMemory:
    def __init__(self, database_url, max_connections=20):
        self.pool = ThreadedConnectionPool(
            1, max_connections, dsn=database_url
        )
        self.init_db()

    @contextmanager
    def getcursor(self):
        con = self.pool.getconn()
        try:
            yield con.cursor()
            con.commit()
        except Exception as e:
            print('Exception:', e)
            con.rollback()
        finally:
            self.pool.putconn(con)

    def init_db(self):
        with self.getcursor() as cur:
            query = """
                DROP TABLE IF EXISTS utc_name_channels;
            """
            cur.execute(query)

    def get_all_utc_name_channels(self):
        with self.getcursor() as cur:
            query = 'SELECT channel_id FROM utc_name_channels'
            cur.execute(query)
            return [
                row[0]\
                for row in cur.fetchall()
            ]

    def add_utc_name_channel(self, channel_id):
        with self.getcursor() as cur:
            query = """
                INSERT INTO utc_name_channels(channel_id) VALUES (%s);
            """
            cur.execute(query, [channel_id])

        
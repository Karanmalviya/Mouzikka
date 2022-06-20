from cx_Oracle import *
from traceback import *


class Model:

    def __init__(self):
        self.song_dict = {}
        self.db_status = True
        self.conn = None
        self.cur = None
        self.connect()

    def connect(self):
        try:
            self.conn = connect("mouzikka/music@localhost/xe")
            print("Connect successfully to the DB")
            self.cur = self.conn.cursor()
        except DatabaseError:
            self.db_status = False
            print("DB error")
            print(format_exc())

    def get_db_status(self):
        return self.db_status

    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Disconnected Successfully the cursor")
        if self.conn is not None:
            self.conn.close()
            print("Disconnected Successfully from the dB")

    def add_song(self, song_name, song_path):
        self.song_dict[song_name] = song_path
        print("model song added ", song_name)

    def get_song_path(self, song_name):
        return self.song_dict[song_name]

    def remove_song(self, song_name):
        self.song_dict.pop(song_name)

    def search_song_in_favourites(self, song_name):
        self.cur.execute("select 1 from myfavourites where song_name = :1", (song_name,))
        song_tuple = self.cur.fetchone()
        return song_tuple is not None

    def add_song_in_favourites(self, song_name, song_path):
        is_song_present = self.search_song_in_favourites(song_name)
        if is_song_present:
            return "Song is already present."
        else:
            self.cur.execute("select max(song_id) from myfavourites")
            last_song_id = self.cur.fetchone()[0]
            if last_song_id is None:
                last_song_id = 0
            last_song_id = last_song_id + 1
            self.cur.execute("insert into myfavourites values (:1,:2,:3)", (last_song_id, song_name, song_path))
            self.conn.commit()
            return "Song added successfully."

    def load_songs_from_favourites(self):
        self.cur.execute("select song_name,song_path from myfavourites")
        song_present = False
        for song_name, song_path in self.cur:
            self.song_dict[song_name] = song_path
            song_present = True
        if song_present:
            return "Song popped from favourites."
        else:
            return "No songs present in the favourites."

    def remove_song_from_favourites(self, song_name):
        self.cur.execute("delete from myfavourites where song_name=:1", (song_name,))
        self.conn.commit()
        if self.cur.rowcount != 0:
            self.song_dict.pop(song_name)
            return "song Deleted successfully."
        else:
            return "No song present with the given song name."




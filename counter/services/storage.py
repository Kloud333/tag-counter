import sqlite3
import pickle
import datetime


def adapter_dict(dict):
    return pickle.dumps(dict)


class Storage:
    table_name = "data"
    sqlite3.register_adapter(dict, adapter_dict)
    sqlite3.register_converter("dict", pickle.loads)

    def __init__(self):
        pass

    def get_tags(self, path):
        db_cursor = self.conn.cursor()
        query = f"select path, date, tags from {self.table_name} where path == ? order by date DESC limit 1"
        db_cursor.execute(query, (path,))

        db_record = db_cursor.fetchone()
        if db_record is None:
            return None

        return pickle.loads(db_record[2])

    def save_tags(self, path, tags_data: {str: int}):
        db_cursor = self.conn.cursor()
        db_cursor.execute(f"insert into {self.table_name} values (?, ?, ?)", (path, str(datetime.datetime.now()), tags_data))
        db_cursor.connection.commit()

    def __enter__(self):
        self.conn = sqlite3.connect('tags.db', detect_types=sqlite3.PARSE_DECLTYPES)
        self.init_database()
        return self

    def __exit__(self, *args):
        self.conn.close()

    def init_database(self):
        db_cursor = self.conn.cursor()
        db_cursor.execute(''' CREATE TABLE IF NOT EXISTS {0} (path text, date text, tags blob)'''.format(self.table_name))
        db_cursor.connection.commit()

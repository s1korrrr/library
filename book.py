import sqlite3
from datetime import datetime, timedelta

class BookSQLData():
    def __init__(self, db_name):
        self.db_name = db_name
        self._conn = None
        self.booking = None
        self.booking_data = None

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def _prepare(self):
        self._conn = self._get_connection()
        return self._conn.cursor()

    def _commit(self):
        self._conn.commit()

    def add(self, name, author):
        book = {}
        book['name'] = name
        book['author'] = author
        print("added: " + book['name'] + " author: " + book['author'])
        print(book)
        c = self._prepare()
        c.execute("INSERT INTO "
                  "book (name, author) "
                  "VALUES ('{name}','{author}')".format(**book))
        self._commit()

    def list(self):
        c = self._prepare()
        res = list(c.execute("SELECT * FROM book"))
        return res

    def update(self, **kwargs):
        # id, new_name, new_author
        c = self._prepare()
        c.execute("UPDATE book "
                  "SET name = '{name}', author = '{author}'"
                  "WHERE id = {id}".format(**kwargs))
        self._commit()

    def del_book(self, id):
        c = self._prepare()
        c.execute("DELETE FROM book WHERE id = {id}".format(id=id))
        self._commit()


    def book(self, nick, id):
        time_now = datetime.now()
        time_delta = timedelta(days=14)
        date_to_give_back = time_now + time_delta
        # print(date_to_give_back)
        self.reserver_by = nick
        self.date_to_give_back = date_to_give_back
        c = self._prepare()
        c.execute("UPDATE book "
                  "SET reserved_by = '{nick}', due_time = '{due_time}'"
                  "WHERE id = {id}".format(nick = nick, id = id, due_time = date_to_give_back))
        self._commit()

import sqlite3


def init_db(db):
    create_table = """
        CREATE TABLE URL_SHORTNER(
        ID INTEGER PRIMARY KEY   AUTOINCREMENT,
        URL  TEXT    NOT NULL,
        SHORT_URL TEXT NOT NULL,
        TLD TEXT NOT NULL
        );
        """
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(create_table)
        except Exception as e:
            print(e)
            pass


def save(url, short_url, tld):
    try:
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            select_row = """
               SELECT URL FROM URL_SHORTNER 
                   WHERE URL =?
            """
            data = (url,)
            result_cursor = cursor.execute(select_row,data)
            row = result_cursor.fetchone()
            if row != None:
                pass
            else:
                insert_row = """
                    INSERT INTO URL_SHORTNER (URL,SHORT_URL,TLD)
                        VALUES (?, ?,  ?)
                    """
                data = (url,short_url,tld)
                result_cursor = cursor.execute(insert_row,data)
    except Exception as e:
        print(e)

def get_url_by_shortcode(url):
    try:
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            select_row = """
                SELECT URL FROM URL_SHORTNER 
                    WHERE SHORT_URL = ?
                """
            data = (url,)
            result_cursor = cursor.execute(select_row,data)
            row = result_cursor.fetchone()
            return row[0]
    except Exception as e:
        print(e)

def get_url_all():
    try:
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            select_row = """
                SELECT SHORT_URL FROM URL_SHORTNER 
                """
            result_cursor = cursor.execute(select_row)
            url_list = []
            for i in result_cursor.fetchall():
                url_list.append(i[0])
            return  url_list
    except Exception as e:
        print(e)

def delete_url(url):
    try:
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            select_row = """
                DELETE  FROM URL_SHORTNER 
                    WHERE SHORT_URL = ?
            """
            data = (url,)
            result_cursor = cursor.execute(select_row,data)
            return  result_cursor.fetchone()
    except Exception as e:
        print(e)

def get_raw_url(url):
    try:
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            select_row = """
                SELECT URL FROM URL_SHORTNER 
                    WHERE SHORT_URL = ?
                """
            data = (url,)
            result_cursor = cursor.execute(select_row,data)
            row = result_cursor.fetchone()
            return row[0]
    except Exception as e:
        print(e)
from config import mysql


class Task:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def get_all(self):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM todos')
        data = cur.fetchall()
        cur.close()
        return data

    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM todos WHERE id=%s', [self.id])
        data = cur.fetchone()
        cur.close()
        return data

    def save(self):
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO todos (name) VALUES (%s)', [self.name])
        mysql.connection.commit()
        cur.close()

    def update(self):
        cur = mysql.connection.cursor()
        cur.execute('UPDATE todos SET name = %s WHERE id = %s',
                    [self.name, self.id])
        mysql.connection.commit()
        cur.close()

    def delete(self):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM todos WHERE id = %s', [self.id])
        mysql.connection.commit()
        cur.close()

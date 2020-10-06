import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()

    def create_to_do_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS Todo (
            id integer PRIMARY KEY,
            title text,
            description text,
            _is_done boolean,
            _is_deleted boolean,
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId integer FOREIGNKEY REFERENCES User(id)
        );
        '''
        self.conn.execute(query)

    def create_user_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS User (
            id integer PRIMARY KEY,
            name text,
            email text
        );
        '''
        self.conn.execute(query)

class TodoModel:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description):
        query = 'INSERT INTO Todo (Title, Description) VALUES (?,?)'
        result = self.conn.execute(query, (text,  description))
        self.conn.commit()
        return self.read(result.lastrowid)
    
    def read(self, item_id):
        if type(item_id) is list:
            format_str = ','.join(['?' for i in item_id])
            query = f'SELECT * FROM Todo WHERE id in ({format_str})'
            return self.conn.execute(query, (*item_id,)).fetchall()
        else:
            query = 'SELECT * FROM Todo WHERE id=?'
            return self.conn.execute(query, (item_id,)).fetchall()

    def update(self, item_id, update_dict):
        # Pass in update_dict with keys as column names and values as new values
        columns = ', '.join([f'{k}=?' for k in update_dict.keys()])[:-1]
        query = f'UPDATE Todo SET {columns} WHERE id=?'
        self.conn.execute(query, (*update_dict.values(), item_id))
        self.conn.commit()

    def delete(self, item_id):
        query = 'DELETE FROM Todo WHERE id=?'
        self.conn.execute(query, (item_id,))
        self.conn.commit()
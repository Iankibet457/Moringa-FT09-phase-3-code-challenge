class Author:
    def __init__(self, id, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be empty")

        from database.connection import get_db_connection
        
        self._name = name
        
        if id is None:
          
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
            self._id = cursor.lastrowid
            conn.commit()
            conn.close()
        else:
            if not isinstance(id, int):
                raise TypeError("ID must be an integer")
            self._id = id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f'<Author {self.name}>'

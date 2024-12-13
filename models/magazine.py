class Magazine:
    def __init__(self, id, name, category="General"):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")

        from database.connection import get_db_connection
        
        self._name = name
        self._category = category
        
        if id is None:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
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

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = new_category

    def __repr__(self):
        return f'<Magazine {self.name}>'

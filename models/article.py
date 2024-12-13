class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        from database.connection import get_db_connection
        
        self._title = title
        self._author_id = author.id  # Assuming author is an instance of Author
        self._magazine_id = magazine.id  # Assuming magazine is an instance of Magazine
        
        # Create new article in database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)', 
                       (title, self._author_id, self._magazine_id))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    def __repr__(self):
        return f'<Article {self.title}>'

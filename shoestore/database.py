import sqlite3
import hashlib
from datetime import datetime


class Database:
    def __init__(self, db_path='shoestore.db'):
        self.db_path = db_path
        self.init_database()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()


        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL,
                is_admin BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('SELECT COUNT(*) FROM users WHERE email = ?', ('admin@admin.com',))
        if cursor.fetchone()[0] == 0:
            admin_password = hashlib.sha256('admin'.encode()).hexdigest()
            cursor.execute('''
                INSERT INTO users (email, password, name, is_admin)
                VALUES (?, ?, ?, ?)
            ''', ('admin@admin.com', admin_password, 'Administrator', 1))

        conn.commit()
        conn.close()
        print("[Database] Database initialized successfully!")

    def create_user(self, email, password, name):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            cursor.execute('''
                INSERT INTO users (email, password, name, is_admin)
                VALUES (?, ?, ?, ?)
            ''', (email, hashed_password, name, 0))

            conn.commit()
            user_id = cursor.lastrowid
            conn.close()
            return user_id
        except sqlite3.IntegrityError:
            return None

    def get_user_by_email(self, email):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                'id': row['id'],
                'email': row['email'],
                'password': row['password'],
                'name': row['name'],
                'is_admin': bool(row['is_admin']),
                'created_at': row['created_at']
            }
        return None

    def verify_user(self, email, password):
        user = self.get_user_by_email(email)
        if not user:
            return None

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if user['password'] == hashed_password:
            return user
        return None

    def get_all_users(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT id, email, name, is_admin, created_at FROM users')
        rows = cursor.fetchall()
        conn.close()

        users = []
        for row in rows:
            users.append({
                'id': row['id'],
                'email': row['email'],
                'name': row['name'],
                'is_admin': bool(row['is_admin']),
                'created_at': row['created_at']
            })
        return users


db = Database()
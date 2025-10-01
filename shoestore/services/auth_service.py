import hashlib


class BaseService:

    def __init__(self):
        self.next_id = 1

    def get_next_id(self):

        current_id = self.next_id
        self.next_id += 1
        return current_id

    def log_action(self, action):

        print(f"[BaseService] {action}")


class AuthService(BaseService):
    def __init__(self):
        super().__init__()
        self.users = [
            {
                'id': 1,
                'email': 'admin@admin.com',
                'password': self._hash_password('admin'),
                'name': 'Administrator',
                'is_admin': True
            }
        ]
        self.next_id = 2

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, email, password, name):
        for user in self.users:
            if user['email'] == email:
                return False

        new_user = {
            'id': self.get_next_id(),
            'email': email,
            'password': self._hash_password(password),
            'name': name,
            'is_admin': False
        }

        self.users.append(new_user)
        self.log_action(f"User registered: {email}")
        print(f"Registration confirmation sent to: {email}")
        return True

    def login_user(self, email, password):
        hashed_password = self._hash_password(password)

        for user in self.users:
            if user['email'] == email and user['password'] == hashed_password:
                self.log_action(f"User logged in: {email}")
                return user

        return None

    def log_action(self, action):
        print(f"[AuthService] {action}")


auth_service = AuthService()
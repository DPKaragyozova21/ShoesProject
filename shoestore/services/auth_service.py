from database import db



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


    def register_user(self, email, password, name):
        user_id = db.create_user(email, password, name)

        if user_id:
            self.log_action(f"User registered: {email}")
            print(f"Registration confirmation sent to: {email}")
            return True
        else:
            self.log_action(f"Registration failed - email exists: {email}")
            return False

    def login_user(self, email, password):
        user = db.verify_user(email, password)

        if user:
            self.log_action(f"User logged in: {email}")
            return user
        else:
            self.log_action(f"Login failed for: {email}")
            return None

    def get_user_by_email(self, email):
        return db.get_user_by_email(email)

    def get_all_users(self):
        return db.get_all_users()

    def log_action(self, action):
        print(f"[AuthService] {action}")


auth_service = AuthService()
class Settings:
    def __init__(self):
        self.database_url = 'sqlite:///db.sqlite3'
        self.debug = True
        self.secret_key = 'your_secret_key_here'

settings = Settings()
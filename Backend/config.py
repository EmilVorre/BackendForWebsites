class Settings:
    PROJECT_NAME: str = "Backend for EmilVorre.dk"
    PROJECT_VERSION: str = "1.0.0"
    ALLOWED_ORIGINS: list = ["http://localhost:5173"]
    HOST: str = "127.0.0.1"
    PORT: int = 8000

settings = Settings()
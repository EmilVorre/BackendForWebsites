class Settings:
    PROJECT_NAME: str = "Backend for EmilVorre.dk"
    PROJECT_VERSION: str = "1.0.0"
    ALLOWED_ORIGINS: list = ["emilvorre.dk", "localhost:5173", "94.145.239.14"]
    HOST: str = "185.172.173.25"
    PORT: int = 8000

settings = Settings()
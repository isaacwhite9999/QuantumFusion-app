# app/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    MAX_ITERATIONS: int = 100
    TOLERANCE: float = 1e-6
    INITIAL_PARAMETERS: str = "0.1,0.1,0.1"  # Comma-separated floats
    SHOTS: int = 1024
    BACKEND: str = "qasm_simulator"
    SEED: int = 42

    class Config:
        env_file = ".env"

settings = Settings()

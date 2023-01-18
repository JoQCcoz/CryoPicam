from pydantic import BaseSettings, Field
from pathlib import Path
from functools import partial
import RPi.GPIO as GPIO


class Settings(BaseSettings):
    dataDir: Path
    sensorPin: int
    frameRate: float = -1

    class Config:
        env_file = 'settings.env'
        env_file_encoding = 'utf-8'

settings = Settings()

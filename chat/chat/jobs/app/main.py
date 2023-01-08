import mongoengine

from pydantic import BaseSetting

class Settings(BaseSetting):
  db_host: str
  db_port: int
  

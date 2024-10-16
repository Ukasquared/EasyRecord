from api.models.engine.database import Database
from api.models.base import Base

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


storage = Database()


print("Registered tables:", Base.metadata.tables.keys())
storage.connect()
from api.models.engine.database import Database

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


storage = Database()


# print("Registered tables:", Base.metadata.tables.keys())
storage.connect()
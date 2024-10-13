import pymongo

from .config import settings

client = pymongo.AsyncMongoClient(settings.MONGO_DB_URI)
app_db = client[settings.DATABASE_NAME]
users_collection = app_db["users"]

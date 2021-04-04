import os

from motor.motor_asyncio import AsyncIOMotorClient

mongo_db_host = os.getenv('MONGO_DB_HOST', 'mongodb')
mongo_db_port = os.getenv('MONGO_DB_PORT', '27017')
mongo_db_url = f'mongodb://{mongo_db_host}:{mongo_db_port}'


mongo_client = AsyncIOMotorClient(mongo_db_url)

mongo_db = mongo_client.url_shorter

url_mapping_collection = mongo_db.url_mapping
short_url_counter_collection = mongo_db.short_url_counter

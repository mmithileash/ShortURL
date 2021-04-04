import os

mongo_db_host = os.getenv('MONGO_DB_HOST', 'mongodb')
mongo_db_port = os.getenv('MONGO_DB_PORT', '27017')
mongo_db_url = f'mongodb://{mongo_db_host}:{mongo_db_port}'

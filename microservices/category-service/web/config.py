import os


PG = {
    "host": os.getenv("POSTGRES_URL"),
    "port": os.getenv("POSTGRES_PORT"),
    "user": os.getenv("POSTGRES_USER"),
    "passwd": os.getenv("POSTGRES_PASSWORD"),
    "db": os.getenv("POSTGRES_DB"),
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{PG['user']}:{PG['passwd']}@{PG['host']}:{PG['port']}/{PG['db']}"
)

rabbit_host = os.getenv('RABBITMQ_HOST', 'localhost')
rabbit_user = os.getenv('RABBITMQ_USER', 'user')
rabbit_pass = os.getenv('RABBITMQ_PASS', 'password')
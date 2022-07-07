from peewee import PostgresqlDatabase, Model

DATABASE = 'postgresql://danilkonkov:@localhost:5432/car_project'
database = PostgresqlDatabase(DATABASE)


def init_app():
    global database
    database = PostgresqlDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = database

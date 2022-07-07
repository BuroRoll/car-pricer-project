# from .database import db
# from models.model import Model
from models.User import User
from models.Car import Car
from .database import database


# def create_db():
#     """Creates database"""
#     db.create_all()
#
#
# def drop_db():
#     """Drop / Clean database - DANGER ACTION"""
#     db.drop_all()
#
#
# def create_model_table():
#     """Create table model in the database"""
#     # Model.__table__.create(db.engine)
#     User.__table__.create(db.engine)
def create_tables():
    with database:
        database.create_tables([User, Car])




def init_app(app):
    for command in [create_tables]:
        app.cli.add_command(app.cli.command()(command))

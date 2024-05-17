#app/db.py
import databases
import ormar
import sqlalchemy

database = databases.Database("sqlite:///db.sqlite3")
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

class Order(ormar.Model):
    class Meta(BaseMeta):
        tablename = "pedidos"

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=128, nullable=False)
    email = ormar.String(max_length=128, nullable=False)
    description = ormar.String(max_length=128, nullable=False)

engine = sqlalchemy.create_engine("sqlite:///db.sqlite3")
metadata.create_all(engine)
from sqlalchemy import event
from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///./academia.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


# SQLite no revisa las llaves foráneas a menos que se lo pidas
@event.listens_for(engine, "connect")
def activar_llaves_foraneas(dbapi_connection, _):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

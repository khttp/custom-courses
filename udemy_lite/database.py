from sqlmodel import SQLModel, Session, create_engine
from udemy_lite.models.user import User, Enrolment
from udemy_lite.models.course import Category, Content, Course

sqlite_file_name = "rf.sqlite3"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


if __name__ == "__main__":
    create_db_and_tables()

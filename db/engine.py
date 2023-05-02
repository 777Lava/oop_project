from sqlalchemy import create_engine
from .ORMModels import Base


engine = create_engine('sqlite:///db.db', echo=True)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

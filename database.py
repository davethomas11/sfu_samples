from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import connection_string

engine = create_engine(connection_string, pool_recycle=3600, echo=True)
db_session = scoped_session(sessionmaker(bind=engine))

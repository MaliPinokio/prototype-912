
from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Session = sessionmaker()
Base = declarative_base()

@contextmanager
def getsession(expunge_all=False):
    session = Session()
    try:
        yield session
        if expunge_all:
            session.expunge_all()
        session.commit()
    except Exception as e:
        print('Exception:', e)
        session.rollback()
    finally:
        session.close()
from data.base import Session, Base

from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists, create_database

from data.model import (
    utc_named_channel
)

def sanitize_postgres_url(url):
    """ Transforms postgres database url in 
        format supported by SQLAlchemy 
    """
    default_prefix = 'postgres:'
    new_prefix = 'postgresql:'
    if url.startswith(default_prefix):
        return new_prefix + url[len(default_prefix):]
    else:
        return url

def get_engine(database_url, echo=True):
    database_url = sanitize_postgres_url(database_url)
    engine = create_engine(database_url, echo=echo)
    Session.configure(bind=engine)
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return engine
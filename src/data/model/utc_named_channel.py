from sqlalchemy import Column, Integer, BigInteger

from data.base import Base

class UTCNamedChannel(Base):
    __tablename__ = 'utc_named_channel'
    
    id = Column(Integer, primary_key=True)
    channel_id = Column(BigInteger, unique=True, nullable=False)
    update_rate = Column(Integer, nullable=False)

    def __init__(self, channel_id, update_rate):
        self.channel_id = channel_id
        self.update_rate = update_rate
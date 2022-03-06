from data.model.utc_named_channel import UTCNamedChannel 

from data.dao_boilerplate import BaseDao

class UTCNamedChannelDao(BaseDao):
    def __init__(self):
        super().__init__(UTCNamedChannel)
    
    def add_channel(self, channel_id, refresh_modulo):
        self.add(UTCNamedChannel(channel_id, refresh_modulo))
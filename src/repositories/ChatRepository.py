from repositories.BaseRepository import BaseRepository

from models.event import Chat


class ChatRepository(BaseRepository):
    def __init__(self):
        self.model = Chat
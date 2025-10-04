from repositories.BaseRepository import BaseRepository

from models.event import Account


class AccountRepository(BaseRepository):
    def __init__(self):
        self.model = Account
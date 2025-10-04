from repositories.BaseRepository import BaseRepository

from models.event import Campaign


class CampaignRepository(BaseRepository):
    def __init__(self):
        self.model = Campaign
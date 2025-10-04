from repositories.BaseRepository import BaseRepository
from db.enums import EventStatusEnum
from models.event import Event


class EventRepository(BaseRepository):
    def __init__(self):
        self.model = Event

    async def update_event_status(self, event_id: int, status: EventStatusEnum):
        return await self.update_one(
            {"id": event_id},
            {"status": status}
        )
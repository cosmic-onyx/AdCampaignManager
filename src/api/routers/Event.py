from fastapi import APIRouter

from repositories.EventRepository import EventRepository


event_router = APIRouter(prefix='/api/v1')


@event_router.get("/event/")
async def get_event_list():
    event_list = await EventRepository().find()
    return {'data': event_list.scalars().all()}
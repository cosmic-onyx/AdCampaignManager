from loguru import logger
from settings.celery_app import celery_app

from db.enums import EventStatusEnum
from repositories.EventRepository import EventRepository
from services.EventRandomizer import EventRandomizer
from tasks.utils import async_to_sync_task


@celery_app.task(name='event_worker.create_random_event')
@async_to_sync_task
async def create_random_event():
    try:
        account_id, chat_id, campaign_id = await EventRandomizer().generate_event()
        logger.info(
            f"""Новый рандомный эвент был успешно сгенерирован
            account_id: {account_id},
            chat_id: {chat_id},
            campaign_id: {campaign_id}
            """
        )
    except Exception as err:
        logger.error(f"Ошибка при генерации эвента: {err}")
        raise err


@celery_app.task(name='event_worker.execution_event')
@async_to_sync_task
async def execution_event(event_id: int):
    try:
        await EventRepository().update_event_status(
            event_id,
            EventStatusEnum.COMPLETED
        )
        logger.info(f"Эвент с id {event_id} был успешно выполнен")
    except Exception as err:
        logger.error(f"Ошибка при выполнении эвента {event_id}: {err}")
        raise err
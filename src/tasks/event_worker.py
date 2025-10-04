import asyncio
from loguru import logger
from settings.celery_app import celery_app

from db.enums import EventStatusEnum
from repositories.EventRepository import EventRepository
from services.EventRandomizer import EventRandomizer


@celery_app.task(name='event_worker.create_random_event')
def create_random_event():
    try:
        asyncio.run(EventRandomizer().generate_event())
        logger.info(
            f"""Новый рандомный эвент был успешно сгенерирован"""
        )
    except Exception as err:
        logger.error(f"Ошибка при генерации эвента: {err}")


@celery_app.task(name='event_worker.execution_event')
def execution_event(event_id: int):
    try:
        asyncio.run(EventRepository().update_event_status(
            event_id,
            EventStatusEnum.COMPLETED
        ))
        logger.info(f"Эвент с id {event_id} был успешно выполнен")
    except Exception as err:
        logger.error(f"Ошибка при выполнении эвента {event_id}: {err}")
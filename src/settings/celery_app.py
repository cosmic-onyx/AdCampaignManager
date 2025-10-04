from celery import Celery

from settings.config import settings


celery_app = Celery(
    "fastapi_celery",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["tasks.event_worker"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    task_always_eager=False,
    worker_concurrency=4,
    result_expires=3600,

    timezone="Europe/Moscow",
    enable_utc=True,

    task_track_started=True,
    task_ignore_result=True,

    task_time_limit=30 * 60,
    task_soft_time_limit=25 * 60,

    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=1000,

    task_default_queue="default",

    task_acks_late=True,
    worker_disable_rate_limits=False,

    worker_log_format="[%(asctime)s: %(levelname)s/%(processName)s] %(message)s",
    worker_task_log_format="[%(asctime)s: %(levelname)s/%(processName)s] [%(task_name)s(%(task_id)s)] %(message)s",
)

celery_app.conf.beat_schedule = {
    'create_random_event': {
        'task': 'event_worker.create_random_event',
        'schedule': 15.0,
    },
}
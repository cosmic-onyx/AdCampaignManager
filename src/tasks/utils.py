from asgiref.sync import async_to_sync


def async_to_sync_task(func):
    def wrapper(*args, **kwargs):
        return async_to_sync(func)(*args, **kwargs)

    return wrapper

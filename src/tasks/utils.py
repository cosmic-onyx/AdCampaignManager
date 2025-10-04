import asyncio
import threading
import nest_asyncio
from asgiref.sync import async_to_sync


nest_asyncio.apply()


def async_to_sync_task(func):
    def wrapper(*args, **kwargs):
        return async_to_sync(func)(*args, **kwargs)

    return wrapper


def run_in_another_thread_task(func):
    def wrapper(*args, **kwargs):
        def run_in_thread():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return loop.run_until_complete(func(*args, **kwargs))

        thread = threading.Thread(target=run_in_thread)
        thread.start()
        thread.join()

        return None
    
    return wrapper

from random import randint

from repositories.AccountRepository import AccountRepository
from repositories.ChatRepository import ChatRepository
from repositories.EventRepository import EventRepository
from repositories.CampaignRepository import CampaignRepository

from services.RedisService import RedisService


class EventRandomizer:
    async def generate_event(self):
        campaign_id = await self.get_random_id(CampaignRepository)
        account_id = await self.get_random_id(
            AccountRepository,
            {"campaign_id": campaign_id}
        )
        chat_id = await self.get_random_id(
            ChatRepository,
            {"campaign_id": campaign_id}
        )

        is_saved = await self.save_cache(account_id, chat_id, campaign_id)
        if is_saved:
            await EventRepository().insert_one(
                {
                    "account_id": account_id,
                    "chat_id": chat_id,
                    "campaign_id": campaign_id
                }
            )

            return account_id, chat_id, campaign_id

    async def get_random_id(self, repository, filters=None):
        if filters is None:
            filters = {}

        objects = await repository().find(filters)
        count_objects = len(objects.scalars().all())
        return randint(1, count_objects)

    async def save_cache(self, account_id, chat_id, campaign_id):
        cache_key = f"{account_id}.{chat_id}"
        res = RedisService().get_data(cache_key)

        if res != campaign_id:
            RedisService().set_data(cache_key, campaign_id)
            return True

        return False
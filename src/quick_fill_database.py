import asyncio
import random
import string
from typing import List


from repositories.CampaignRepository import CampaignRepository
from repositories.AccountRepository import AccountRepository
from repositories.ChatRepository import ChatRepository


COUNT_CAMPAIGN = 10
COUNT_ACCOUNT_IN_CAMPAIGN = 50
COUNT_CHAT_IN_CAMPAIGN = 50


class DataGenerator:
    @staticmethod
    def generate_campaign_name() -> str:
        adjectives = ['Digital', 'Social', 'Marketing', 'Creative', 'Advanced', 'Premium', 'Elite', 'Dynamic']
        nouns = ['Campaign', 'Strategy', 'Initiative', 'Project', 'Program', 'Drive', 'Push', 'Effort']
        number = random.randint(1, 9999)
        return f"{random.choice(adjectives)} {random.choice(nouns)} {number}"
    
    @staticmethod
    def generate_username() -> str:
        prefixes = ['user', 'account', 'profile', 'member', 'client']
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"{random.choice(prefixes)}_{suffix}"
    
    @staticmethod
    def generate_chat_title() -> str:
        prefixes = ['Chat', 'Group', 'Channel', 'Room', 'Discussion']
        topics = ['Marketing', 'Sales', 'Support', 'General', 'Updates', 'News', 'Team']
        number = random.randint(1, 999)
        return f"{random.choice(prefixes)} {random.choice(topics)} {number}"


class DatabaseFiller:
    def __init__(self):
        self.data_generator = DataGenerator()
    
    async def create_campaigns(self, count: int) -> List[int]:
        campaign_ids = []
        
        for i in range(count):
            campaign_name = self.data_generator.generate_campaign_name()
            campaign_data = {"name": campaign_name}
            
            try:
                result = await CampaignRepository().insert_one(campaign_data)
                campaign_id = result.inserted_primary_key[0]
                if campaign_id:
                    campaign_ids.append(campaign_id)
            except Exception as e:
                print(f"Ошибка при создании кампании {campaign_name}: {e}")
        
        return campaign_ids
    
    async def create_accounts_for_campaign(self, campaign_id: int, count: int) -> List[int]:
        account_ids = []

        for i in range(count):
            username = self.data_generator.generate_username()
            account_data = {
                "username": username,
                "campaign_id": campaign_id
            }
                
            try:
                result = await AccountRepository().insert_one(account_data)
                account_id = result.inserted_primary_key[0]
                if account_id:
                    account_ids.append(account_id)
            except Exception as e:
                print(f"  Ошибка при создании аккаунта {username}: {e}")
        
        return account_ids
    
    async def create_chats_for_campaign(self, campaign_id: int, count: int) -> List[int]:
        chat_ids = []
            
        for i in range(count):
            chat_title = self.data_generator.generate_chat_title()
            chat_data = {
                "title": chat_title,
                "campaign_id": campaign_id
            }
                
            try:
                result = await ChatRepository().insert_one(chat_data)
                chat_id = result.inserted_primary_key[0]
                if chat_id:
                    chat_ids.append(chat_id)
            except Exception as e:
                print(f"  Ошибка при создании чата {chat_title}: {e}")
        
        return chat_ids
    
    async def fill_database(self):
        campaign_ids = await self.create_campaigns(COUNT_CAMPAIGN)
        
        if not campaign_ids:
            print("Не удалось создать ни одной кампании. Завершение работы.")
            return
        
        print(f"\nУспешно создано {len(campaign_ids)} кампаний")
        print("-" * 50)

        total_accounts = 0
        total_chats = 0
        
        for campaign_id in campaign_ids:
            account_ids = await self.create_accounts_for_campaign(campaign_id, COUNT_ACCOUNT_IN_CAMPAIGN)
            total_accounts += len(account_ids)

            chat_ids = await self.create_chats_for_campaign(campaign_id, COUNT_CHAT_IN_CAMPAIGN)
            total_chats += len(chat_ids)

        print("\n" + "=" * 50)
        print("ЗАПОЛНЕНИЕ БАЗЫ ДАННЫХ ЗАВЕРШЕНО")
        print("=" * 50)
        print(f"Создано кампаний: {len(campaign_ids)}")
        print(f"Создано аккаунтов: {total_accounts}")
        print(f"Создано чатов: {total_chats}")
        print(f"Общее количество записей: {len(campaign_ids) + total_accounts + total_chats}")


async def main():
    filler = DatabaseFiller()
    await filler.fill_database()


if __name__ == "__main__":
    asyncio.run(main())
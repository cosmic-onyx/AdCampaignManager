# PostedAPI

## Установка и запуск

1. Склонируйте репозиторий
```bash
git clone https://github.com/cosmic-onyx/AdCampaignManager.git
```
2. Настройте переменные окружения, 
скопируйте содержимое .env.example и вставьте в новый созданный вами файл .env

3. Запустите проект
```bash
docker compose up -d --build
```

## Запуск тестов

```bash
cd src

python -m pytest
```

## API Эндпоинты
### События (Event)

#### Получить список всех статей
- **GET** `/api/v1/event/`
- **Описание**: Получить список всех эвентов и их статусы
- **Ответ**: `200 OK`
  ```json
  [
    {
      "id": 1,
      "account_id": 15,
      "chat_id": 23,
      "campaign_id": 1,
      "status": "выполнено/невыполнено",
      "created_at": "2025-10-04T10:00:00Z"
    }
  ]
  ```
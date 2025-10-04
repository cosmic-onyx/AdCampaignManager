import enum


class EventStatusEnum(str, enum.Enum):
    NOT_COMPLETED = "не выполнено"
    COMPLETED = "выполнено"
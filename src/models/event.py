from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base
from db.enums import EventStatusEnum
from db.annotated import str_an, unique_str_an


class Campaign(Base):
    name: Mapped[unique_str_an]


class Account(Base):
    username: Mapped[unique_str_an]
    campaign_id: Mapped[int] = mapped_column(ForeignKey('campaigns.id'))


class Chat(Base):
    title: Mapped[str_an]
    campaign_id: Mapped[int] = mapped_column(ForeignKey('campaigns.id'))


class Event(Base):
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.id'))
    chat_id: Mapped[int] = mapped_column(ForeignKey('chats.id'))
    campaign_id: Mapped[int] = mapped_column(ForeignKey('campaigns.id'))
    status: Mapped[str] = mapped_column(
        String, nullable=True, default=EventStatusEnum.NOT_COMPLETED
    )
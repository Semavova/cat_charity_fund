from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text

from app.core.db import Base

DESCRIPTION = (
    "Пользователь: {user_id}, "
    "Внесенная сумма: {full_amount}, "
    "Использовано: {invested_amount}, "
    "Завершено: {fully_invested}"
)


class Donation(Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    close_date = Column(DateTime)

    def __repr__(self):
        return DESCRIPTION.format(
            user_id=self.user_id,
            full_amount=self.full_amount,
            invested_amount=self.invested_amount,
            fully_invested=self.fully_invested
        )

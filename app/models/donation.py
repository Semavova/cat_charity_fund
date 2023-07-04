from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import BaseClass

DESCRIPTION = (
    "Пользователь: {user_id}, "
    "Внесенная сумма: {full_amount}, "
    "Использовано: {invested_amount}, "
    "Завершено: {fully_invested}"
)


class Donation(BaseClass):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self):
        return DESCRIPTION.format(
            user_id=self.user_id,
            full_amount=self.full_amount,
            invested_amount=self.invested_amount,
            fully_invested=self.fully_invested
        )

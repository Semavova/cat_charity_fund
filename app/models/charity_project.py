from sqlalchemy import Column, String, Text

from app.models.base import BaseClass

DESCRIPTION = (
    "Название: {name}, "
    "Необходимая сумма: {full_amount}, "
    "Уже собрано: {invested_amount}, "
    "Завершен сбор: {fully_invested}"
)


class CharityProject(BaseClass):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return DESCRIPTION.format(
            name=self.name,
            full_amount=self.full_amount,
            invested_amount=self.invested_amount,
            fully_invested=self.fully_invested
        )

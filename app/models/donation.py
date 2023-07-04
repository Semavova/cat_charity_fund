from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import BaseClass

DESCRIPTION = (
    "Пользователь: {user_id}, "
    "{invested}"
)


class Donation(BaseClass):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self):
        return DESCRIPTION.format(
            user_id=self.user_id,
            invested=super().__repr__()
        )

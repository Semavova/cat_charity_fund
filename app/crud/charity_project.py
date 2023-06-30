from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.donation_service import set_close
from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get(
        self,
        charity_id: int,
        session: AsyncSession,
    ) -> Optional[CharityProject]:
        """Возвращает объект CharityProject из БД по id"""
        db_obj = await session.execute(
            select(CharityProject).where(CharityProject.id == charity_id)
        )
        return db_obj.scalars().first()

    async def update(
        self,
        db_obj: CharityProject,
        obj_in,
        session: AsyncSession,
    ) -> CharityProject:
        """Обновляет объект CharityProject и возвращает обновленный объект."""
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict()
        for field in obj_data:
            if field in update_data and update_data[field] is not None:
                setattr(db_obj, field, update_data[field])
        db_obj = set_close(db_obj)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
        self,
        db_obj: CharityProject,
        session: AsyncSession,
    ) -> CharityProject:
        """Удаляет объект CharityProject по id."""
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        """Возвращает project_id по имени проекта"""
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )

        return db_project_id.scalar()


charity_project_crud = CRUDCharityProject(CharityProject)

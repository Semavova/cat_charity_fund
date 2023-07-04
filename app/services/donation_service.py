from datetime import datetime
from typing import List, Optional

from app.models.base import Base


def investment(
    target: Base,
    sources: List[Base],
) -> List[Optional[Base]]:
    """
    Перебирает открытые проекты/донаты, вычисляет сумму перевода.
    Переводит средства из донатов в проекты.
    Закрывает исчерпанные донаты и заполненные проекты.
    """
    modified = []
    for source in sources:
        fund = min(
            target.full_amount - target.invested_amount,
            source.full_amount - source.invested_amount
        )
        if not fund:
            break
        for investment in [target, source]:
            investment.invested_amount += fund
            if investment.invested_amount == investment.full_amount:
                investment.fully_invested = True
                investment.close_date = datetime.now()
        modified.append(source)
    return modified

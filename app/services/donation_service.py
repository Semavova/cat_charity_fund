from datetime import datetime
from typing import List


def investment(
    target,
    sources,
) -> List:
    """
    Перебирает открытые проекты/донаты, вычисляет сумму перевода.
    Переводит средства из донатов в проекты.
    Закрывает исчерпанные донаты и заполненные проекты.
    """
    modified = []
    for open_obj in sources:
        fund = min(
            target.full_amount - target.invested_amount,
            open_obj.full_amount - open_obj.invested_amount
        )
        investments = [target, open_obj]
        for investment in investments:
            investment.invested_amount += fund
            if investment.invested_amount == investment.full_amount:
                investment.fully_invested = True
                investment.close_date = datetime.now()
        modified.append(open_obj)
    modified.append(target)
    return modified

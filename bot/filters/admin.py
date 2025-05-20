from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsBotAdminFilter(BaseFilter):
    def __init__(self, admin_id: int):
        self.admin_id = admin_id 

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.admin_id
    

class IsBotAdminsFilter(BaseFilter):
    def __init__(self, admin_ids: list[int]):
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

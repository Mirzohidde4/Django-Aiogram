from asgiref.sync import sync_to_async
from main.models import AdminMod, BotSettings


async def get_admin_id():
    return await sync_to_async(lambda: AdminMod.objects.first())()


async def get_admins_ids():
    admins = await sync_to_async(lambda: list(AdminMod.objects.all()))()
    return [admin.user_id for admin in admins]


async def get_bot_token():
    bot_settings = await sync_to_async(lambda: BotSettings.objects.first())()
    return bot_settings.token if bot_settings else None